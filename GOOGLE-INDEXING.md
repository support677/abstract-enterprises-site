# Google Indexing API for job pages

Runs entirely on Netlify. No keys in this repo.

- `netlify/lib/indexing.mjs` signs a service-account JWT and calls the Indexing API.
- `netlify/functions/indexing-sync-background.mjs` checks every `*-jobs*` URL in sitemap.xml (plus every URL already logged):
  new/changed JobPosting -> URL_UPDATED; validThrough passed or page removed (404/410/redirect) -> URL_DELETED (once).
  Hub pages without JobPosting markup are never submitted (Google only accepts JobPosting/BroadcastEvent pages).
- `netlify/functions/deploy-succeeded.mjs` runs the sync after every production deploy.
- `netlify/functions/indexing-daily.mjs` runs it daily at 6:15 AM ET (expiry sweep + quota retries).
- Log/state: Airtable Pipeline base, table "Google Indexing" (tblboEbboVviSLFJN). Google Result = Accepted means Google took it.

Netlify env vars (production, functions scope): GOOGLE_INDEXING_SA_EMAIL, GOOGLE_INDEXING_SA_KEY, INDEXING_SECRET, AIRTABLE_PAT.
Manual run: POST https://www.abstractenterprisessecuritysystems.com/.netlify/functions/indexing-sync-background
with header `x-indexing-secret: <INDEXING_SECRET>` and optional body `{"force": true}`.

Renewing postings: push validThrough forward on the JobPosting pages (do not change datePosted); the next deploy re-notifies Google.
