#!/usr/bin/env python3
"""Render + upload hero videos for one shard of the site's pages.
Usage: python batch.py <shard> <shards> [limit]   (env: R2_*, AESS_SITE, KOKORO_DIR)
Writes results/<shard>.json with the metadata inject.py needs."""
import json, os, sys, traceback, concurrent.futures as cf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import boto3
import pages

D = os.path.dirname(os.path.abspath(__file__))
SITE = os.environ.get("AESS_SITE", os.path.abspath(os.path.join(D, "..", "..")))
shard, shards = int(sys.argv[1]), int(sys.argv[2])
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 0
only_s = os.environ.get("HV_ONLY", "")
if only_s.startswith("@"):   # only=@redo.txt -> one slug per line in that file
    only_s = ",".join(open(os.path.join(D, only_s[1:])).read().split())
only = [x for x in only_s.split(",") if x]
todo = only or pages.candidates(SITE, force=os.environ.get("HV_FORCE") == "1")
todo = [p for i, p in enumerate(todo) if i % shards == shard]
if limit:
    todo = todo[:limit]
print(f"shard {shard}/{shards}: {len(todo)} pages", flush=True)

s3 = boto3.client("s3", endpoint_url=f"https://{os.environ['R2_ACCOUNT']}.r2.cloudflarestorage.com",
                  aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
                  aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"], region_name="auto")
OUT = os.path.join(D, "out", str(shard)); os.makedirs(OUT, exist_ok=True)


def one(slug):
    import hero_video
    m = hero_video.render(os.path.join(SITE, slug + ".html"), OUT)
    made = m.get("slug", slug)          # index.html renders as "home"; store it under the page's own file name
    if made != slug:
        for ext in (".mp4", ".jpg"):
            os.replace(os.path.join(OUT, made + ext), os.path.join(OUT, slug + ext))
    for ext, ct in ((".mp4", "video/mp4"), (".jpg", "image/jpeg")):
        s3.upload_file(os.path.join(OUT, slug + ext), os.environ.get("R2_BUCKET", "aess-videos"), f"hero/{slug}{ext}",
                       ExtraArgs={"ContentType": ct, "CacheControl": "public, max-age=86400"})
        os.remove(os.path.join(OUT, slug + ext))
    return dict(v=2, slug=slug, seconds=m["seconds"], service=m["service"],
                place=m["neighborhood"] or (m["area"][1] if m["area"] else ""), price=m["price"])


results, failed = [], []
workers = int(os.environ.get("HV_WORKERS", "3"))
with cf.ProcessPoolExecutor(workers) as ex:
    futs = {ex.submit(one, p): p for p in todo}
    for i, fu in enumerate(cf.as_completed(futs), 1):
        try:
            results.append(fu.result())
            print(f"[{i}/{len(todo)}] ok {futs[fu]}", flush=True)
        except Exception:
            failed.append(futs[fu]); traceback.print_exc()
os.makedirs(os.path.join(D, "results"), exist_ok=True)
json.dump(dict(ok=results, failed=failed), open(os.path.join(D, "results", f"{shard}.json"), "w"))
print(f"done: {len(results)} ok, {len(failed)} failed")
