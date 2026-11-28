// Background function (up to 15 min): keeps Google's Indexing API in step with the job pages.
//  - new or changed posting            -> URL_UPDATED
//  - validThrough passed               -> URL_DELETED (once)
//  - page removed (404/410/redirect)   -> URL_DELETED (once)
// Every notification and Google's answer is logged in the Airtable "Google Indexing" table
// (Pipeline base), which is also the memory of what was last sent for each URL.
// Triggered by deploy-succeeded (every production deploy), indexing-daily (expiry sweep),
// or by hand: POST /.netlify/functions/indexing-sync-background with header x-indexing-secret.
// Body (optional JSON): {"force": true} re-sends URL_UPDATED for every live posting.
import { getAccessToken, publish, jobUrlsFromSitemap, inspectPage, isExpired } from "../lib/indexing.mjs";

const BASE_ID = "appWu6U6PaYn1iQ0U";
const TABLE = "Google Indexing";
const MAX_PER_RUN = 180; // Google's default quota is 200 publish calls a day

const at = (path, opts = {}) => fetch(`https://api.airtable.com/v0/${BASE_ID}/${encodeURIComponent(TABLE)}${path}`, {
  ...opts, headers: { Authorization: `Bearer ${process.env.AIRTABLE_PAT}`, "Content-Type": "application/json" },
}).then(async (r) => { const d = await r.json(); if (!r.ok) throw new Error(`airtable ${r.status} ${JSON.stringify(d)}`); return d; });

async function loadLog() {
  const rows = new Map(); let offset = "";
  do {
    const d = await at(`?pageSize=100${offset ? `&offset=${offset}` : ""}`);
    for (const rec of d.records) if (rec.fields.URL) rows.set(rec.fields.URL, rec);
    offset = d.offset || "";
  } while (offset);
  return rows;
}

async function saveLog(updates, creates) {
  for (let i = 0; i < updates.length; i += 10)
    await at("", { method: "PATCH", body: JSON.stringify({ records: updates.slice(i, i + 10), typecast: true }) });
  for (let i = 0; i < creates.length; i += 10)
    await at("", { method: "POST", body: JSON.stringify({ records: creates.slice(i, i + 10), typecast: true }) });
}

export default async (req) => {
  const secret = process.env.INDEXING_SECRET;
  if (!secret || req.headers.get("x-indexing-secret") !== secret) { console.log("INDEXING: bad or missing secret"); return; }
  let opts = {}; try { opts = await req.json(); } catch {}
  const trigger = opts.trigger || "manual";
  const nowIso = new Date().toISOString();

  const log = await loadLog();
  const urls = new Set(await jobUrlsFromSitemap());
  for (const u of log.keys()) urls.add(u); // also re-check anything we notified before

  const token = await getAccessToken();
  const updates = [], creates = [];
  let sent = 0, skipped = 0;

  for (const url of urls) {
    const prev = log.get(url); const pf = prev?.fields || {};
    const page = await inspectPage(url);
    let type = null, state;

    if (page.error) { console.log("INDEXING fetch error", url, page.status); continue; }
    if (page.gone) { state = "Removed"; if (pf["Last Type"] === "URL_UPDATED") type = "URL_DELETED"; }
    else if (!page.job) { state = "Hub (no JobPosting, not submitted)"; if (pf["Last Type"] === "URL_UPDATED") type = "URL_DELETED"; }
    else if (isExpired(page.validThrough)) { state = "Expired"; if (pf["Last Type"] !== "URL_DELETED") type = "URL_DELETED"; }
    else {
      state = "Live";
      if (opts.force || pf["Content Hash"] !== page.hash || pf["Last Type"] !== "URL_UPDATED" || pf["Google Result"] !== "Accepted") type = "URL_UPDATED";
    }

    const fields = { URL: url, Status: state, "Valid Through": page.validThrough || pf["Valid Through"] || "", "Last Checked": nowIso };
    if (page.hash) fields["Content Hash"] = page.hash;
    if (type && sent < MAX_PER_RUN) {
      const res = await publish(token, url, type); sent++;
      Object.assign(fields, {
        "Last Type": type, "Last Notified": nowIso, Trigger: trigger,
        "Google Result": res.ok ? "Accepted" : `Error ${res.status}`, "Google Response": res.text,
      });
      console.log("INDEXING", type, url, res.status);
    } else if (type) { skipped++; fields["Google Result"] = "Waiting (daily quota)"; }

    if (prev) updates.push({ id: prev.id, fields }); else creates.push({ fields });
  }
  await saveLog(updates, creates);
  console.log(`INDEXING done: ${sent} sent, ${skipped} held for quota, ${urls.size} URLs checked (${trigger})`);
};
