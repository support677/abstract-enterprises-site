// Website contact-form gate.
// Every form on the site posts here instead of straight to Web3Forms.
// Real leads are forwarded to Web3Forms (same inbox as before).
// Spam (SEO / marketing pitches, bots that tick the hidden honeypot,
// link dumps) is dropped. The sender still sees "success" so they
// have no reason to retry, and every blocked submission is written to
// the function log in full, so a wrongly blocked lead can be found.

// Server-side key. Set WEB3FORMS_KEY in Netlify env to rotate it;
// once rotated, the old key in the page source stops working and
// bots that post directly to Web3Forms are cut off.
const KEY = process.env.WEB3FORMS_KEY || "88890030-1770-483e-a622-0e054d8e14b1";

// Phrases that only show up in sales pitches to the business, not in
// requests from customers who need security work done.
const SPAM_PATTERNS = [
  /\bseo\b/i,
  /search engine optimi[sz]/i,
  /back ?links?\b/i,
  /guest post/i,
  /(website|site|web) traffic/i,
  /drop in (website |site )?traffic/i,
  /(major|critical|technical) errors? (on|in|with|that)/i,
  /errors? (on|in) your (website|site)/i,
  /your (website|site)('s)? (performance|ranking|traffic|design|errors?)/i,
  /(rank|ranking|rankings) (on|in|higher)/i,
  /first page of (google|bing)/i,
  /google (ranking|my business ranking|maps ranking)/i,
  /(quick|free) (website |seo )?audit/i,
  /website (audit|redesign|revamp|makeover)/i,
  /web ?(design|development) (services|agency|company)/i,
  /digital marketing/i,
  /marketing (services|agency|proposal)/i,
  /social media (marketing|management)/i,
  /lead generation (services|agency)/i,
  /\b(virtual assistant|outsourc(e|ing)|offshore team)\b/i,
  /\b(app|mobile app|software) development (services|company|agency)\b/i,
  /business (funding|loan|line of credit)/i,
  /merchant cash advance/i,
  /\b(crypto|bitcoin|forex)\b/i,
];

// Weak signals: normal people write these too, so it takes two of them.
const WEAK_PATTERNS = [
  /schedule a (quick )?(call|meeting)/i,
  /thanks? (&|and) best regards/i,
  /^\s*re:\s/im,
  /let me know if you('| a)?re interested/i,
  /(happy|glad) to (send|share) (you )?(the )?(details|report|errors|solutions)/i,
  /\b(proposal|pricing) for your (business|website|company)\b/i,
];

// Attribution fields stamped onto every form by /js/ph.js (Module 3).
// They are not typed by the customer, so the spam check ignores them.
const ATTR_KEYS = [
  "ph_distinct_id", "ph_session_id", "page_slug", "lead_service", "lead_area", "lead_region",
  "utm_source", "utm_medium", "utm_campaign", "utm_content", "first_landing", "first_referrer", "aess_test",
];
const PH_KEY = process.env.POSTHOG_KEY || "phc_wJyrBYx3gBLsevhvXiMhFUSFt2JjFeK6iSXyhrHRnogj";

// Server-side lead event: ad-blockers can stop the browser event, not this one.
// Carries the visitor's distinct_id so it joins their pageviews, replay and first-touch source.
async function captureLead(data) {
  const props = { $lib: "aess-contact-fn", source_form: "website" };
  for (const k of ATTR_KEYS) if (data[k]) props[k] = String(data[k]).slice(0, 300);
  if (data.ph_session_id) props.$session_id = data.ph_session_id;
  props.has_phone = !!(data.phone || data.Phone || data.tel);
  props.has_email = !!(data.email || data.Email);
  try {
    await fetch("https://us.i.posthog.com/i/v0/e/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        api_key: PH_KEY,
        event: "lead_submitted",
        distinct_id: data.ph_distinct_id || `anon-lead-${Date.now()}`,
        properties: props,
      }),
    });
  } catch (e) {
    console.log("POSTHOG LEAD EVENT FAILED", String(e));
  }
  // Same lead to the attribution store (Airtable "Web Touches" via aess-hcp-webhooks),
  // with phone/email so the nightly match can tie it to the HCP customer and paid jobs.
  if (!process.env.TOUCH_KEY) { console.log("TOUCH_KEY not set; form touch not recorded"); return; }
  try {
    const touch = { ...props, touch_id: `form-${data.ph_session_id || ""}-${Date.now()}`.slice(0, 80),
      ts: new Date().toISOString(), phone: data.phone || data.Phone || data.tel || "",
      email: data.email || data.Email || "", name: data.name || data.Name || data.full_name || "",
      test: data.aess_test === "1" };
    const r = await fetch("https://aess-hcp-webhooks.onrender.com/touch/form", {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-Touch-Key": process.env.TOUCH_KEY },
      body: JSON.stringify(touch),
      signal: AbortSignal.timeout(6000),
    });
    if (!r.ok) console.log("FORM TOUCH FAILED", r.status);
  } catch (e) {
    console.log("FORM TOUCH ERROR", String(e));
  }
}

// Turn any body shape (JSON, form-urlencoded, multipart) into a plain object.
async function readBody(req) {
  const type = (req.headers.get("content-type") || "").toLowerCase();
  if (type.includes("application/json")) {
    try { return await req.json(); } catch { return {}; }
  }
  try {
    const fd = await req.formData();
    const out = {};
    for (const [k, v] of fd.entries()) if (typeof v === "string") out[k] = v;
    return out;
  } catch {
    return {};
  }
}

function spamReason(data) {
  const bot = data.botcheck;
  if (bot && bot !== "false" && bot !== "") return "honeypot";

  // Look at everything the sender typed (skip our own hidden fields).
  const skip = new Set(["access_key", "subject", "from_name", "page", "Page", "redirect", "botcheck", ...ATTR_KEYS]);
  const text = Object.entries(data)
    .filter(([k]) => !skip.has(k))
    .map(([, v]) => String(v))
    .join("\n");

  for (const re of SPAM_PATTERNS) if (re.test(text)) return `phrase ${re}`;

  const weak = WEAK_PATTERNS.filter((re) => re.test(text));
  if (weak.length >= 2) return `weak ${weak.join(" ")}`;

  const links = (text.match(/(https?:\/\/|\bwww\.)\S+/gi) || []).filter((u, i, a) => a.indexOf(u) === i).length;
  if (links >= 3) return "links";

  const blocked = (process.env.SPAM_BLOCKLIST || "")
    .split(",").map((s) => s.trim().toLowerCase()).filter(Boolean);
  const email = String(data.email || "").toLowerCase();
  if (email && blocked.some((b) => email.endsWith(b))) return "blocklist";

  return null;
}

function reply(req, ok) {
  const wantsJson = (req.headers.get("accept") || "").includes("json") ||
    (req.headers.get("content-type") || "").includes("json");
  if (wantsJson || req.headers.get("sec-fetch-mode") === "cors") {
    return Response.json({ success: ok, message: ok ? "Form submitted" : "Please call us" });
  }
  // Plain HTML form post with JavaScript off: send them back to the page.
  const back = req.headers.get("referer") || "/";
  return new Response(null, { status: 303, headers: { Location: back.split("#")[0] + (back.includes("?") ? "&" : "?") + "sent=1" } });
}

export default async (req) => {
  if (req.method !== "POST") return new Response("Method not allowed", { status: 405 });

  const data = await readBody(req);
  const why = spamReason(data);

  if (why) {
    console.log("BLOCKED", why, JSON.stringify(data));
    return reply(req, true);
  }

  data.access_key = KEY;
  delete data.botcheck;

  // One readable line in the lead email: which page/service/area and which channel produced it.
  const src = [data.utm_source, data.utm_medium, data.utm_campaign].filter(Boolean).join(" / ");
  const ref = data.first_referrer && data.first_referrer !== "$direct" ? data.first_referrer : "direct";
  if (data.page_slug) {
    data["Lead source"] = `${data.lead_service || "?"} — ${data.lead_area || "?"} (${data.page_slug}) · ` +
      (src ? `campaign ${src}` : `first came from ${ref}`) +
      (data.first_landing && data.first_landing !== data.page_slug ? ` · first landed on ${data.first_landing}` : "");
  }
  await captureLead(data);
  // End-to-end test submissions (aess_test=1) are tracked but never emailed to the office.
  if (data.aess_test === "1") return reply(req, true);

  try {
    const r = await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(data),
    });
    const d = await r.json().catch(() => ({}));
    if (!d.success) console.log("WEB3FORMS FAILED", r.status, JSON.stringify(d), JSON.stringify(data));
    return reply(req, !!d.success);
  } catch (e) {
    console.log("WEB3FORMS ERROR", String(e), JSON.stringify(data));
    return reply(req, false);
  }
};

export const config = { path: "/api/contact" };
