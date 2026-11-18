// Adds the Google Ads call-tracking script to every HTML page at the edge, so the 2,800+ existing
// pages and every new page the factory builds get it without editing each file.
// Also reports every visit that came from a Google Ads click (gclid/gbraid/wbraid) to the
// click-fraud guard on aess-hcp-webhooks, which blocks IPs that click the ads over and over.
import type { Config, Context } from "https://edge.netlify.com";

const TAG = '<script src="/js/gads-calls.js" defer></script>';
const CLICK_URL = "https://aess-hcp-webhooks.onrender.com/gads/click";

function reportAdClick(req: Request, context: Context) {
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  const gclid = url.searchParams.get("gclid") || url.searchParams.get("gbraid") || url.searchParams.get("wbraid");
  if (!gclid) return;
  const key = Netlify.env.get("TOUCH_KEY");
  if (!key) return;
  const geo = (context.geo || {}) as Record<string, unknown>;
  const body = JSON.stringify({
    ip: context.ip,
    gclid,
    path: url.pathname,
    zip: geo.postalCode || "",
    city: geo.city || "",
    ua: (req.headers.get("user-agent") || "").slice(0, 200),
  });
  context.waitUntil(
    fetch(CLICK_URL, { method: "POST", headers: { "Content-Type": "application/json", "X-Touch-Key": key }, body })
      .then((r) => { if (!r.ok) console.log("AD CLICK REPORT FAILED", r.status); })
      .catch((e) => console.log("AD CLICK REPORT ERROR", String(e))),
  );
}

export default async (req: Request, context: Context) => {
  try { reportAdClick(req, context); } catch (e) { console.log("AD CLICK REPORT ERROR", String(e)); }
  const res = await context.next();
  const type = res.headers.get("content-type") || "";
  if (!type.includes("text/html")) return res;

  const html = await res.text();
  if (html.includes("/js/gads-calls.js") || !html.includes("</head>")) {
    return new Response(html, res);
  }
  const headers = new Headers(res.headers);
  headers.delete("content-length");
  return new Response(html.replace("</head>", TAG + "</head>"), {
    status: res.status,
    statusText: res.statusText,
    headers,
  });
};

export const config: Config = {
  path: "/*",
  excludedPath: ["/js/*", "/css/*", "/v/*", "/videos/*", "/images/*", "/img/*", "/.netlify/*", "/*.xml", "/*.txt", "/*.json"],
};
