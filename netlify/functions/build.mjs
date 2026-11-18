// "Build your own system" tracked link.
// Customers get abstractenterprisessecuritysystems.com/b/CODE in a text.
// A tap logs the click on their row in the Airtable "Build Links" table, then
// sends them to their pre-loaded price page (Target), e.g.
// /lorex-camera-installation-prices-queens?build=CN301A-1TW-AB1:4&ref=CODE
// The redirect always happens, even if logging fails, and only ever to this site.

const SITE = "https://www.abstractenterprisessecuritysystems.com";
const FALLBACK = "/name-brand-cameras";
const BASE_ID = "appWu6U6PaYn1iQ0U";
const TABLE_ID = "tbltYY98JM22xvs9v";
const F_TARGET = "fldKDsllWKihXk96E";
const F_CLICKS = "flduRr4BU0e7LCdD3";
const F_FIRST_CLICKED = "fldSftVBfkdv5BJnY";

function safeTarget(t) {
  if (!t) return FALLBACK;
  if (t.startsWith(SITE + "/")) t = t.slice(SITE.length);
  return /^\/[A-Za-z0-9]/.test(t) && !t.startsWith("//") ? t : FALLBACK;
}

async function lookupAndLog(code) {
  const token = process.env.AIRTABLE_PAT;
  if (!token || !/^[A-Za-z0-9-]{3,40}$/.test(code)) return null;
  const headers = { Authorization: `Bearer ${token}`, "Content-Type": "application/json" };
  const api = `https://api.airtable.com/v0/${BASE_ID}/${TABLE_ID}`;
  const formula = encodeURIComponent(`{Code}='${code}'`);
  const found = await fetch(`${api}?filterByFormula=${formula}&maxRecords=1&returnFieldsByFieldId=true`, { headers })
    .then((r) => r.json());
  const rec = found.records && found.records[0];
  if (!rec) return null;
  const fields = { [F_CLICKS]: (rec.fields[F_CLICKS] || 0) + 1 };
  if (!rec.fields[F_FIRST_CLICKED]) fields[F_FIRST_CLICKED] = new Date().toISOString();
  await fetch(`${api}/${rec.id}`, { method: "PATCH", headers, body: JSON.stringify({ fields }) }).catch(() => {});
  return rec.fields[F_TARGET] || null;
}

export default async (req) => {
  const path = new URL(req.url).pathname;
  const code = decodeURIComponent(path.replace(/^\/b\/?/, "").split("/")[0] || "");
  let target = null;
  if (code) {
    try {
      target = await Promise.race([lookupAndLog(code), new Promise((r) => setTimeout(() => r(null), 2500))]);
    } catch (e) {
      console.error("build link lookup failed", e);
    }
  }
  return new Response(null, {
    status: 302,
    headers: { Location: safeTarget(target), "Cache-Control": "no-store" },
  });
};

export const config = { path: ["/b/*"] };
