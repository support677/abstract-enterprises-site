// Adds the Google Ads call-tracking script to every HTML page at the edge, so the 2,800+ existing
// pages and every new page the factory builds get it without editing each file.
import type { Config, Context } from "https://edge.netlify.com";

const TAG = '<script src="/js/gads-calls.js" defer></script>';

export default async (_req: Request, context: Context) => {
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
