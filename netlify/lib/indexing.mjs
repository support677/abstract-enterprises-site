// Google Indexing API helper for the job pages.
// Credentials come from Netlify environment variables (never the repo):
//   GOOGLE_INDEXING_SA_EMAIL  service account email
//   GOOGLE_INDEXING_SA_KEY    service account private key (PEM; "\n" escapes are fine)
// Google only accepts the Indexing API for pages with JobPosting (or BroadcastEvent) markup,
// so hub pages without a JobPosting are never submitted.
import crypto from "node:crypto";

export const SITE = "https://www.abstractenterprisessecuritysystems.com";
const SCOPE = "https://www.googleapis.com/auth/indexing";
const TOKEN_URL = "https://oauth2.googleapis.com/token";
const PUBLISH_URL = "https://indexing.googleapis.com/v3/urlNotifications:publish";

const b64url = (s) => Buffer.from(s).toString("base64").replace(/=+$/, "").replace(/\+/g, "-").replace(/\//g, "_");

export async function getAccessToken() {
  const email = process.env.GOOGLE_INDEXING_SA_EMAIL;
  const key = (process.env.GOOGLE_INDEXING_SA_KEY || "").replace(/\\n/g, "\n");
  if (!email || !key) throw new Error("GOOGLE_INDEXING_SA_EMAIL / GOOGLE_INDEXING_SA_KEY not set");
  const now = Math.floor(Date.now() / 1000);
  const unsigned = b64url(JSON.stringify({ alg: "RS256", typ: "JWT" })) + "." +
    b64url(JSON.stringify({ iss: email, scope: SCOPE, aud: TOKEN_URL, iat: now, exp: now + 3600 }));
  const sig = crypto.createSign("RSA-SHA256").update(unsigned).sign(key, "base64")
    .replace(/=+$/, "").replace(/\+/g, "-").replace(/\//g, "_");
  const r = await fetch(TOKEN_URL, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer", assertion: `${unsigned}.${sig}` }),
  });
  const d = await r.json();
  if (!r.ok) throw new Error(`token ${r.status}: ${JSON.stringify(d)}`);
  return d.access_token;
}

export async function publish(token, url, type) {
  const r = await fetch(PUBLISH_URL, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
    body: JSON.stringify({ url, type }),
  });
  const text = await r.text();
  return { ok: r.ok, status: r.status, text: text.slice(0, 900) };
}

// Pull the job page URLs from the live sitemap (every *-jobs or *-jobs-<area> page).
export async function jobUrlsFromSitemap() {
  const xml = await fetch(`${SITE}/sitemap.xml`).then((r) => r.text());
  const urls = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1].trim());
  return urls.filter((u) => /-jobs(-[a-z0-9-]+)?$/.test(new URL(u).pathname));
}

// Fetch one page and read its JobPosting (if any).
export async function inspectPage(url) {
  const r = await fetch(url, { redirect: "manual" });
  if (r.status === 404 || r.status === 410) return { gone: true, status: r.status };
  if (r.status >= 300 && r.status < 400) return { gone: true, status: r.status, redirect: r.headers.get("location") };
  if (!r.ok) return { error: true, status: r.status };
  const html = await r.text();
  let job = null;
  for (const m of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
    try { const d = JSON.parse(m[1]); if (d["@type"] === "JobPosting") { job = d; break; } } catch {}
  }
  if (!job) return { job: null, status: r.status };
  // Hash the posting itself plus the visible page body, so any content change re-notifies Google.
  const body = html.replace(/<script[\s\S]*?<\/script>/g, "").replace(/\s+/g, " ");
  const hash = crypto.createHash("sha256").update(JSON.stringify(job) + body).digest("hex").slice(0, 32);
  return { job, hash, validThrough: job.validThrough || "", status: r.status };
}

// validThrough like "2027-02-18T23:59" is read as New York time.
export function isExpired(validThrough, now = new Date()) {
  if (!validThrough) return false;
  const v = /[zZ]|[+-]\d\d:?\d\d$/.test(validThrough) ? validThrough : `${validThrough}${validThrough.length <= 10 ? "T23:59:59" : ""}-05:00`;
  const t = Date.parse(v);
  return Number.isFinite(t) && t < now.getTime();
}
