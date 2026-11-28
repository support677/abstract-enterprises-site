// Job application form on the careers / job pages.
// Saves each applicant to the Airtable "Hiring" table (AESS Pipeline base) with the resume attached,
// so applications land in the same place the hiring agents already work from.
// Bots that tick the hidden honeypot are dropped (they still see "success").

const BASE_ID = "appWu6U6PaYn1iQ0U";
const TABLE_ID = "tbllrXx3kz3xBTUzv"; // Hiring
const RESUME_FIELD = "fldII5uAofpUj4IFT"; // Resume (attachments)
const MAX_BYTES = 4 * 1024 * 1024;
const OK_TYPES = /\.(pdf|docx?|jpe?g|png|heic)$/i;

const clean = (v, n = 500) => String(v ?? "").replace(/\s+/g, " ").trim().slice(0, n);

function json(ok, status = 200, message = "") {
  return Response.json({ success: ok, message }, { status });
}

export default async (req) => {
  if (req.method !== "POST") return new Response("Method not allowed", { status: 405 });
  const token = process.env.AIRTABLE_PAT;
  if (!token) { console.log("APPLY: AIRTABLE_PAT not set"); return json(false, 502, "not configured"); }

  let fd;
  try { fd = await req.formData(); } catch { return json(false, 400, "bad form"); }
  const bot = fd.get("botcheck");
  if (bot && bot !== "false") { console.log("APPLY BLOCKED honeypot"); return json(true); }

  const first = clean(fd.get("first_name"), 60), last = clean(fd.get("last_name"), 60);
  const phone = clean(fd.get("phone"), 40), email = clean(fd.get("email"), 120);
  if (!first || !last || !phone) return json(false, 400, "missing fields");

  const position = clean(fd.get("position"), 120);
  const today = new Date().toLocaleDateString("en-CA", { timeZone: "America/New_York" });
  const experience = [
    `Years of paid experience: ${clean(fd.get("experience_years"), 60) || "not given"}`,
    `Certifications: ${clean(fd.get("certifications"), 300) || "none listed"}`,
    clean(fd.get("message"), 2000),
  ].filter(Boolean).join("\n");
  const notes = [
    `Applied on the website: ${clean(fd.get("source_page"), 200)} (${clean(fd.get("area"), 40)})`,
    `License / vehicle: ${clean(fd.get("transportation"), 80)}`,
  ].join("\n");

  const headers = { Authorization: `Bearer ${token}`, "Content-Type": "application/json" };
  const fields = {
    Name: `${first} ${last}`,
    Phone: phone,
    Location: clean(fd.get("location"), 120),
    "Position Applied": position,
    Applied: today,
    Source: "Website",
    Transportation: clean(fd.get("transportation"), 80) || undefined,
    Experience: experience,
    Notes: notes,
  };
  if (email && /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) fields.Email = email;

  let recId;
  try {
    const r = await fetch(`https://api.airtable.com/v0/${BASE_ID}/${TABLE_ID}`, {
      method: "POST", headers, body: JSON.stringify({ records: [{ fields }], typecast: true }),
    });
    const d = await r.json();
    if (!r.ok) { console.log("APPLY CREATE FAILED", r.status, JSON.stringify(d), JSON.stringify(fields)); return json(false, 502, "save failed"); }
    recId = d.records[0].id;
  } catch (e) {
    console.log("APPLY CREATE ERROR", String(e), JSON.stringify(fields));
    return json(false, 502, "save failed");
  }

  const file = fd.get("resume");
  if (file && typeof file === "object" && file.size > 0) {
    if (file.size > MAX_BYTES || !OK_TYPES.test(file.name || "")) {
      console.log("APPLY RESUME SKIPPED", file.name, file.size);
    } else {
      try {
        const b64 = Buffer.from(await file.arrayBuffer()).toString("base64");
        const u = await fetch(`https://content.airtable.com/v0/${BASE_ID}/${recId}/${RESUME_FIELD}/uploadAttachment`, {
          method: "POST", headers,
          body: JSON.stringify({ contentType: file.type || "application/octet-stream", file: b64, filename: file.name.slice(0, 120) }),
        });
        if (!u.ok) console.log("APPLY RESUME UPLOAD FAILED", u.status, await u.text());
      } catch (e) {
        console.log("APPLY RESUME ERROR", String(e));
      }
    }
  }
  return json(true);
};

export const config = { path: "/api/apply" };
