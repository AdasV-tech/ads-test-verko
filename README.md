# Billboard

Public, no-UI photo billboard. Anyone who opens the link sees photos
crossfading full-screen — nothing local, works on any device.

## One-time setup

1. Create a repo (e.g. `adasv-tech/billboard`) and push this folder:

```
cd billboard-site
git init
git add .
git commit -m "billboard init"
git branch -M main
git remote add origin https://github.com/adasv-tech/billboard.git
git push -u origin main
```

2. GitHub repo → Settings → Pages → Source: `main` branch, `/ (root)`.

3. Custom domain (same pattern as cards.verko.lt):
   - Edit `CNAME` in this repo if you want a different subdomain than
     `board.verko.lt`.
   - In Cloudflare DNS for verko.lt, add a CNAME record:
     `board` → `adasv-tech.github.io`, proxy status = DNS only (grey cloud)
     until GitHub Pages issues the SSL cert, then you can proxy it (orange).
   - In GitHub repo Settings → Pages, enter `board.verko.lt` as the custom
     domain and enable "Enforce HTTPS" once it's issued.

## Updating the photos (day to day)

1. Drop image files into `images/` (jpg/png/webp/gif).
2. Run:
   ```
   python3 generate-manifest.py
   ```
   Optionally set the seconds between photos: `python3 generate-manifest.py 8`
3. Commit and push:
   ```
   git add .
   git commit -m "update photos"
   git push
   ```
4. Live in ~30–60s (GitHub Pages build time). Anyone with the URL already
   open will pick up the new set automatically within 2 minutes — no
   refresh needed, since the page re-polls `manifest.json` on its own.

## Notes

- Keep photos reasonably sized (under ~2–3MB each) — it's a plain git repo,
  not object storage, so a huge library will bloat clone size.
- To run it on an actual screen/kiosk unattended: open the URL, press F11
  for browser fullscreen, disable sleep on that machine.
