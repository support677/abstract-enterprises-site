// Automatic equipment cut sheet.
//
//   /cutsheet?i=N3T-8LA2*8&i=R52-8PA4&i=LUM-J02*8&c=Jane%20Doe&a=12%20Main%20St&t=Camera%20System
//
// i = one item per param: a Product Catalog Model, or a Generic Price Book
//     Item / Cut Sheet Title, optionally followed by *qty. Case-insensitive.
// c = customer name, a = address, t = title (all optional).
// check=1 adds an internal list of anything not found or missing a photo.
//
// Photos, blurbs and specs come live from Airtable every time, so a product
// photo is stored once (Product Catalog > Photo, or Generic Price Book > Photo)
// and never uploaded again. No prices are shown. Generic items never show the
// word "generic" or the internal model number.

const BASE_ID = "appWu6U6PaYn1iQ0U";
const CATALOG = {
  id: "tblZ8gryQG003vxzP",
  model: "fld4lU925M8ATEivC",
  brand: "fldKCQzjyCcREyATg",
  product: "fld1XDBk2mA8HrkWZ",
  category: "fldADzRHTKdH7YDbU",
  photo: "fldct4zaMAXomTjQU",
  blurb: "fldHpdyUzNY89uAfO",
  specs: "fld4PSkW2ujHUsujh",
};
const GENERIC = {
  id: "tbl3T7f17ph79l6Im",
  item: "flddxA5CklH1WRWPM",
  category: "fldL9dwQ5Qcfx65zg",
  photo: "fldthWbxGzgrttb4W",
  title: "fldWAz9JDwtsn9lzH",
  blurb: "fldXjUkz31YdWFvBk",
  specs: "fldt7ieJHhaFkLbg1",
};

const esc = (s) =>
  String(s ?? "").replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[ch]);
const norm = (s) => String(s ?? "").trim().toLowerCase();
const sel = (v) => (v && typeof v === "object" ? v.name : v) || "";

async function allRecords(tableId, token) {
  const out = [];
  let offset;
  do {
    const u = new URL(`https://api.airtable.com/v0/${BASE_ID}/${tableId}`);
    u.searchParams.set("returnFieldsByFieldId", "true");
    u.searchParams.set("pageSize", "100");
    if (offset) u.searchParams.set("offset", offset);
    const r = await fetch(u, { headers: { Authorization: `Bearer ${token}` } });
    if (!r.ok) throw new Error(`Airtable ${tableId} ${r.status}`);
    const j = await r.json();
    out.push(...(j.records || []));
    offset = j.offset;
  } while (offset);
  return out;
}

function parseItems(params) {
  const raw = params.getAll("i").flatMap((v) => v.split("|"));
  return raw
    .map((s) => s.trim())
    .filter(Boolean)
    .map((s) => {
      const m = s.match(/^(.*?)\s*\*\s*(\d+)$/);
      return m ? { key: m[1], qty: Number(m[2]) } : { key: s, qty: 1 };
    });
}

function specRows(text) {
  return String(text || "")
    .split(/\n+/)
    .map((l) => l.trim())
    .filter(Boolean)
    .map((l) => {
      const i = l.indexOf(":");
      return i > 0 && i < 40 ? [l.slice(0, i).trim(), l.slice(i + 1).trim()] : ["", l];
    });
}

const ICON = `<svg viewBox="0 0 64 64" width="72" height="72" aria-hidden="true"><rect x="8" y="14" width="48" height="36" rx="6" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="32" cy="32" r="9" fill="none" stroke="currentColor" stroke-width="3"/></svg>`;

function card(it) {
  const photo = it.photo
    ? `<img src="${esc(it.photo)}" alt="${esc(it.name)}" loading="eager">`
    : `<div class="noimg">${ICON}</div>`;
  const specs = specRows(it.specs);
  const table = specs.length
    ? `<table>${specs.map(([k, v]) => `<tr>${k ? `<th>${esc(k)}</th><td>${esc(v)}</td>` : `<td colspan="2">${esc(v)}</td>`}</tr>`).join("")}</table>`
    : "";
  return `<section class="card">
  <div class="ph">${photo}</div>
  <div class="body">
    <div class="top"><h2>${esc(it.name)}</h2>${it.qty > 1 ? `<span class="qty">Qty ${it.qty}</span>` : ""}</div>
    ${it.sub ? `<p class="sub">${esc(it.sub)}</p>` : ""}
    ${it.blurb ? `<p>${esc(it.blurb)}</p>` : ""}
    ${table}
  </div>
</section>`;
}

function page({ items, missing, customer, address, title, check }) {
  const today = new Date().toLocaleDateString("en-US", { timeZone: "America/New_York", year: "numeric", month: "long", day: "numeric" });
  const report = check && missing.length
    ? `<aside class="check"><b>Internal check (not shown without check=1):</b><ul>${missing.map((m) => `<li>${esc(m)}</li>`).join("")}</ul></aside>`
    : "";
  return `<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>${esc(title || "Equipment Cut Sheet")} | Abstract Enterprises Security Systems</title>
<style>
:root{--ink:#14202b;--mut:#5b6773;--line:#dfe4ea;--acc:#0b5cab;--bg:#fff}
*{box-sizing:border-box}body{margin:0;background:#f3f5f8;color:var(--ink);font:15px/1.45 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:860px;margin:0 auto;padding:16px}
header{background:var(--bg);border-radius:12px;padding:18px 20px;display:flex;gap:16px;align-items:center;justify-content:space-between;flex-wrap:wrap;border:1px solid var(--line)}
header img{height:46px;width:auto}
.meta{text-align:right;font-size:13px;color:var(--mut)}.meta b{color:var(--ink);font-size:16px;display:block}
h1{font-size:22px;margin:20px 4px 10px}
.card{background:var(--bg);border:1px solid var(--line);border-radius:12px;display:grid;grid-template-columns:200px 1fr;gap:18px;padding:16px;margin:0 0 14px;break-inside:avoid;page-break-inside:avoid}
.ph{display:flex;align-items:center;justify-content:center;background:#fafbfc;border-radius:8px;min-height:180px}
.ph img{max-width:100%;max-height:200px;object-fit:contain}
.noimg{color:#9aa6b2}
.top{display:flex;justify-content:space-between;gap:10px;align-items:baseline}
h2{font-size:18px;margin:0}.qty{background:#e8f1fb;color:var(--acc);font-weight:600;border-radius:20px;padding:2px 10px;font-size:13px;white-space:nowrap}
.sub{color:var(--mut);margin:4px 0 8px;font-size:13px}
p{margin:6px 0 10px}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{text-align:left;padding:5px 8px;border-top:1px solid var(--line);vertical-align:top}th{width:34%;color:var(--mut);font-weight:600}
footer{text-align:center;color:var(--mut);font-size:12px;margin:18px 0 8px}
.check{background:#fff6e0;border:1px solid #f0c36d;border-radius:10px;padding:10px 14px;margin:10px 0}
.print{position:fixed;right:16px;bottom:16px;background:var(--acc);color:#fff;border:0;border-radius:24px;padding:10px 18px;font-weight:600;cursor:pointer}
@media (max-width:600px){.card{grid-template-columns:1fr}.meta{text-align:left}}
@media print{body{background:#fff}.wrap{padding:0}.print,.check{display:none}header,.card{border-color:#ccc}}
</style></head><body><div class="wrap">
<header><img src="/images/logo.png" alt="Abstract Enterprises Security Systems">
<div class="meta">${customer ? `<b>${esc(customer)}</b>` : ""}${address ? `${esc(address)}<br>` : ""}${today}</div></header>
<h1>${esc(title || "Equipment Cut Sheet")}</h1>
${report}
${items.map(card).join("\n")}
<footer>Abstract Enterprises Security Systems · (800) 486-0943 · abstractenterprisessecuritysystems.com · Licensed &amp; Insured · NYS License #12000287431</footer>
</div><button class="print" onclick="window.print()">Save / Print PDF</button></body></html>`;
}

export default async (req) => {
  const params = new URL(req.url).searchParams;
  const token = process.env.AIRTABLE_PAT;
  const wanted = parseItems(params);
  const html = (body, status = 200) =>
    new Response(body, { status, headers: { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store", "X-Robots-Tag": "noindex" } });

  if (!token) return html("<p>Cut sheets are not configured yet (AIRTABLE_PAT missing).</p>", 500);
  if (!wanted.length) return html("<p>No items. Add ?i=MODEL*qty for each item.</p>", 400);

  let catalog, generic;
  try {
    [catalog, generic] = await Promise.all([allRecords(CATALOG.id, token), allRecords(GENERIC.id, token)]);
  } catch (e) {
    console.error("cutsheet airtable", e.message);
    return html("<p>Couldn't load the product library right now. Try again in a minute.</p>", 502);
  }

  const byModel = new Map(catalog.map((r) => [norm(r.fields[CATALOG.model]), r]));
  const byGeneric = new Map();
  for (const r of generic) {
    byGeneric.set(norm(r.fields[GENERIC.item]), r);
    if (r.fields[GENERIC.title]) byGeneric.set(norm(r.fields[GENERIC.title]), r);
  }

  const items = [];
  const missing = [];
  for (const w of wanted) {
    const c = byModel.get(norm(w.key));
    if (c) {
      const f = c.fields;
      const photo = (f[CATALOG.photo] || [])[0];
      if (!photo) missing.push(`${w.key}: no photo in Product Catalog`);
      items.push({
        qty: w.qty,
        name: f[CATALOG.product] || f[CATALOG.model],
        sub: [f[CATALOG.brand], f[CATALOG.model]].filter(Boolean).join(" · "),
        blurb: f[CATALOG.blurb],
        specs: f[CATALOG.specs],
        photo: photo && ((photo.thumbnails && photo.thumbnails.large && photo.thumbnails.large.url) || photo.url),
      });
      continue;
    }
    const g = byGeneric.get(norm(w.key));
    if (g) {
      const f = g.fields;
      const photo = (f[GENERIC.photo] || [])[0];
      if (!photo) missing.push(`${w.key}: no photo in Generic Price Book`);
      items.push({
        qty: w.qty,
        name: f[GENERIC.title] || f[GENERIC.item],
        sub: sel(f[GENERIC.category]),
        blurb: f[GENERIC.blurb],
        specs: f[GENERIC.specs],
        photo: photo && ((photo.thumbnails && photo.thumbnails.large && photo.thumbnails.large.url) || photo.url),
      });
      continue;
    }
    missing.push(`${w.key}: not in Product Catalog or Generic Price Book`);
  }

  if (!items.length) return html(`<p>None of those items are in the product library: ${esc(wanted.map((w) => w.key).join(", "))}</p>`, 404);

  return html(
    page({
      items,
      missing,
      customer: params.get("c"),
      address: params.get("a"),
      title: params.get("t"),
      check: params.get("check") === "1",
    })
  );
};

export const config = { path: "/cutsheet" };
