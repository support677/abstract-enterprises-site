// Daily sweep: sends URL_DELETED for any job posting whose validThrough has passed,
// and retries anything that was held back by Google's daily quota.
import { SITE } from "../lib/indexing.mjs";

export default async () => {
  const r = await fetch(`${SITE}/.netlify/functions/indexing-sync-background`, {
    method: "POST",
    headers: { "x-indexing-secret": process.env.INDEXING_SECRET || "", "Content-Type": "application/json" },
    body: JSON.stringify({ trigger: "daily" }),
  });
  console.log("indexing-daily ->", r.status);
};

export const config = { schedule: "15 11 * * *" }; // 6:15 AM New York (UTC)
