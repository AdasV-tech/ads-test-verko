#!/usr/bin/env python3
"""
Scans the images/ folder and rewrites manifest.json with what it finds.
Run this after adding or removing photos, then git add/commit/push.

Usage:
    python3 generate-manifest.py            # keeps current interval (default 5s)
    python3 generate-manifest.py 8          # sets interval to 8 seconds
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
IMAGES_DIR = ROOT / "images"
MANIFEST = ROOT / "manifest.json"
VALID_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

def main():
    interval = 5
    if MANIFEST.exists():
        try:
            existing = json.loads(MANIFEST.read_text())
            interval = existing.get("interval", 5)
        except Exception:
            pass
    if len(sys.argv) > 1:
        interval = float(sys.argv[1])

    files = sorted(
        f.name for f in IMAGES_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in VALID_EXT
    )

    manifest = {"interval": interval, "images": files}
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"manifest.json updated: {len(files)} photo(s), interval={interval}s")

if __name__ == "__main__":
    main()
