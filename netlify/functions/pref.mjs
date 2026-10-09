// Google Preferred Source tracked link.
// Each customer gets abstractenterprisessecuritysystems.com/g/CODE.
// A tap logs the click on their row in the Airtable "Preferred Source Links"
// table, then sends them straight to Google's source-preferences page.
// The redirect always happens, even if logging fails.

const GOOGLE_URL =
  "https://www.google.com/preferences/source?q=abstractenterprisessecuritysystems.com";
const BASE_ID = "appWu6U6PaYn1iQ0U";
const TABLE_ID = "tblgixzoWkolVkYwL";
const F_CODE = "fld7WNJoguKhzlfUJ";
const F_FIRST_CLICKED = "fldCDpGvyeIREXmio";
const F_CLICKS = "flddQ5D7EVQKktaqn";

async function logClick(code) {
  const token = process.env.AIRTABLE_PAT;
  if (!token || !/^[A-Za-z0-9_-]{3,40}$/.test(code)) return;

  const headers = { Authorization: `Bearer ${token}`, "Content-Type": "application/json" };
  const api = `https://api.airtable.com/v0/${BASE_ID}/${TABLE_ID}`;

  const formula = encodeURIComponent(`{Code}='${code}'`);
  const found = await fetch(
    `${api}?filterByFormula=${formula}&maxRecords=1&returnFieldsByFieldId=true`,
    { headers }
  ).then((r) => r.json());

  const rec = found.records && found.records[0];
  const now = new Date().toISOString();

  if (rec) {
    const fields = { [F_CLICKS]: (rec.fields[F_CLICKS] || 0) + 1 };
    if (!rec.fields[F_FIRST_CLICKED]) fields[F_FIRST_CLICKED] = now;
    await fetch(`${api}/${rec.id}`, { method: "PATCH", headers, body: JSON.stringify({ fields }) });
  } else {
    // Unknown code (typo or postcard/QR code): still record it.
    await fetch(api, {
      method: "POST",
      headers,
      body: JSON.stringify({
        fields: { [F_CODE]: code, [F_CLICKS]: 1, [F_FIRST_CLICKED]: now },
      }),
    });
  }
}

export default async (req) => {
  const path = new URL(req.url).pathname;
  const code = decodeURIComponent(path.replace(/^\/g\/?/, "").split("/")[0] || "");

  if (code) {
    try {
      await Promise.race([logClick(code), new Promise((r) => setTimeout(r, 2500))]);
    } catch (e) {
      console.error("pref click log failed", e);
    }
  }

  return new Response(null, {
    status: 302,
    headers: { Location: GOOGLE_URL, "Cache-Control": "no-store" },
  });
};

export const config = { path: ["/g", "/g/*"] };
