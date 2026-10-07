#!/usr/bin/env python3
"""Snapshot the public URLs and SEO metadata of the site as it is served today.

Run once against the last Publii export, before the generator replaced it:

    python3 tools/snapshot.py

Writes:
  tools/url-inventory.txt  every public URL, one per line: "<kind> <path>"
  tools/baseline-meta.json title/description/canonical/OG/twitter/robots/dates
                           of every HTML page, keyed by URL path

tools/check_urls.py compares a fresh build against both files.
Needs beautifulsoup4 + lxml (snapshot only, not needed by the build).
"""
import json
import subprocess
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent

# Old Publii theme files. The new templates no longer load them and nothing
# outside the theme links to them; robots.txt already disallowed /assets.
RETIRED_PREFIXES = ("assets/",)
SKIP_NAMES = (".DS_Store",)


def tracked_files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True)
    return [line for line in out.stdout.splitlines() if line]


def url_for(path):
    if path == "index.html":
        return "/"
    if path.endswith("/index.html"):
        return "/" + path[: -len("index.html")]
    return "/" + path


def kind_for(path):
    if path.endswith(".html"):
        return "page"
    if path.startswith("media/"):
        return "media"
    if path.startswith("sdet/"):
        return "sdet"
    return "file"


def page_meta(html):
    soup = BeautifulSoup(html, "lxml")
    meta = {"title": soup.title.get_text() if soup.title else None}
    for tag in soup.find_all("meta"):
        key = tag.get("name") or tag.get("property")
        if not key:
            continue
        if key == "description" or key == "robots" or key.startswith(("og:", "twitter:")):
            meta[key] = tag.get("content")
    canonical = soup.find("link", rel="canonical")
    if canonical:
        meta["canonical"] = canonical.get("href")
    for script in soup.find_all("script", type="application/ld+json"):
        data = json.loads(script.string)
        if data.get("@type") == "Article":
            meta["datePublished"] = data.get("datePublished")
            meta["dateModified"] = data.get("dateModified")
    return meta


def main():
    lines, retired, baseline = [], [], {}
    for path in sorted(tracked_files()):
        if Path(path).name in SKIP_NAMES:
            continue
        url = url_for(path)
        if path.startswith(RETIRED_PREFIXES):
            retired.append(url)
            continue
        kind = kind_for(path)
        lines.append(f"{kind} {url}")
        if kind == "page" and not path.startswith("sdet/"):
            baseline[url] = page_meta((ROOT / path).read_text(encoding="utf-8"))

    header = [
        "# Public URLs of fachrul.id as exported by Publii (last publish 2024-02-09).",
        "# Format: <kind> <url-path>. A path ending in / is served by <path>index.html.",
        "# tools/check_urls.py fails the build if any of these stops existing.",
        "# Retired (old Publii theme files, replaced by the new templates):",
    ] + [f"#   {url}" for url in retired]
    (ROOT / "tools/url-inventory.txt").write_text("\n".join(header + lines) + "\n", encoding="utf-8")
    (ROOT / "tools/baseline-meta.json").write_text(
        json.dumps(baseline, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"{len(lines)} URLs inventoried, {len(retired)} retired, {len(baseline)} pages with metadata")


if __name__ == "__main__":
    main()
