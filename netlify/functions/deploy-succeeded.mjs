// Runs after every successful Netlify deploy. On production deploys it starts the
// Google Indexing sync, which notifies Google about any job page that changed or was removed.
import { SITE } from "../lib/indexing.mjs";

export default async (req) => {
  let ctx = "";
  try { ctx = (await req.json())?.payload?.context || ""; } catch {}
  if (ctx && ctx !== "production") return new Response("skip " + ctx);
  const r = await fetch(`${SITE}/.netlify/functions/indexing-sync-background`, {
    method: "POST",
    headers: { "x-indexing-secret": process.env.INDEXING_SECRET || "", "Content-Type": "application/json" },
    body: JSON.stringify({ trigger: "deploy" }),
  });
  console.log("deploy-succeeded -> indexing sync", r.status);
  return new Response("ok");
};
