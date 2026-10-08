#!/usr/bin/env python3
"""Snapshot the public URLs and SEO metadata of the site as it is served today.

Reads the last Publii export from git (SOURCE_REV), so it can be re-run
after the generator has replaced the HTML:

    python3 tools/snapshot.py

GitHub Pages builds this repo with Jekyll, so the served URLs are the files
minus anything Jekyll hides (paths with a part starting with "." or "_"),
plus an .html rendering of every markdown file.

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


SOURCE_REV = "68da9a3"  # last commit served from the Publii export


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def tracked_files():
    return [line for line in git("ls-tree", "-r", "--name-only", SOURCE_REV).splitlines() if line]


def read(path):
    return git("show", f"{SOURCE_REV}:{path}")


def hidden_by_jekyll(path):
    return any(part.startswith((".", "_")) for part in path.split("/"))


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


def feed_urls():
    """Item URLs of both feeds and the page URLs of the sitemap."""
    import re
    import xml.etree.ElementTree as ET

    atom = "{http://www.w3.org/2005/Atom}"
    xml_feed = ET.fromstring(read("feed.xml").encode("utf-8"))
    json_feed = json.loads(read("feed.json"))
    sitemap = read("sitemap.xml")
    return {
        "feed.xml": [e.find(atom + "id").text for e in xml_feed.findall(atom + "entry")],
        "feed.json": [item["url"] for item in json_feed["items"]],
        "sitemap.xml": re.findall(r"<url>\s*<loc>([^<]+)</loc>", sitemap),
    }


def main():
    lines, retired, baseline = [], [], {}
    for path in sorted(tracked_files()):
        if hidden_by_jekyll(path):
            continue
        url = url_for(path)
        if path.startswith(RETIRED_PREFIXES):
            retired.append(url)
            continue
        kind = kind_for(path)
        lines.append(f"{kind} {url}")
        if path.endswith(".md"):
            lines.append(f"jekyll {url[:-3]}.html")
        if kind == "page" and not path.startswith("sdet/"):
            baseline[url] = page_meta(read(path))

    baseline["__feeds__"] = feed_urls()

    header = [
        "# Public URLs of fachrul.id as exported by Publii (last publish 2024-02-09).",
        "# Format: <kind> <url-path>. A path ending in / is served by <path>index.html;",
        "# kind 'jekyll' is rendered by GitHub Pages from the .md file of the same name.",
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
