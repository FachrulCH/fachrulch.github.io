#!/usr/bin/env python3
"""Prove the built site still serves every URL the Publii site served.

    python3 tools/check_urls.py

Checks, against tools/url-inventory.txt and tools/baseline-meta.json:
  1. every inventoried URL exists at the same path, in the same form
     (/slug/ as slug/index.html, /file.ext as a file);
  2. every page keeps its title, description, canonical, robots, Open Graph,
     twitter and article dates (keys absent in the baseline are not compared;
     leading/trailing whitespace is ignored, Publii padded some tag titles);
  3. feed.xml and feed.json parse, and still carry the same item URLs;
  4. sitemap.xml parses and lists every URL it listed before;
  5. every root-relative link, image and script in the built pages resolves.
Exits non-zero on any failure. Uses only the standard library.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://fachrul.id"
ATOM = "{http://www.w3.org/2005/Atom}"
SITEMAP = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.meta, self.refs, self.in_title, self.title = {}, [], False, ""
        self.ld = []
        self.in_ld = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key and (key in ("description", "robots") or key.startswith(("og:", "twitter:"))):
                self.meta[key] = a.get("content")
        elif tag == "link" and a.get("rel") == "canonical":
            self.meta["canonical"] = a.get("href")
        elif tag == "script" and a.get("type") == "application/ld+json":
            self.in_ld = True
            self.ld.append("")
        for attr in ("href", "src"):
            if a.get(attr):
                self.refs.append(a[attr])
        if a.get("srcset"):
            self.refs += [part.strip().split(" ")[0] for part in a["srcset"].split(",") if part.strip()]

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script":
            self.in_ld = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_ld:
            self.ld[-1] += data

    def result(self):
        meta = dict(self.meta, title=self.title)
        for block in self.ld:
            data = json.loads(block)
            if data.get("@type") == "Article":
                meta["datePublished"] = data.get("datePublished")
                meta["dateModified"] = data.get("dateModified")
        return meta


def file_for(url):
    path = unquote(urlsplit(url).path)
    return ROOT / (path.lstrip("/") + "index.html" if path.endswith("/") else path.lstrip("/"))


def main():
    failures = []
    inventory = [line.split(" ", 1) for line in (ROOT / "tools/url-inventory.txt").read_text().splitlines()
                 if line and not line.startswith("#")]
    baseline = json.loads((ROOT / "tools/baseline-meta.json").read_text(encoding="utf-8"))
    feeds = baseline.pop("__feeds__")

    # 1. URLs
    kinds = {}
    excluded = re.findall(r"^\s+-\s+(\S+)", (ROOT / "_config.yml").read_text(), re.M)
    for kind, url in inventory:
        kinds[kind] = kinds.get(kind, 0) + 1
        if url.lstrip("/").split("/")[0] in excluded:
            failures.append(f"URL excluded from the Jekyll build by _config.yml: {url}")
        if kind == "jekyll":  # GitHub Pages renders it from the markdown file
            url = url[: -len(".html")] + ".md"
        target = file_for(url)
        if not target.is_file():
            failures.append(f"missing URL: {url} (expected {target.relative_to(ROOT)})")
        if not url.endswith("/") and file_for(url + "/").is_file():
            failures.append(f"URL changed form: {url} is now a directory")
    print(f"[1] URLs: {len(inventory)} inventoried ({', '.join(f'{v} {k}' for k, v in sorted(kinds.items()))})")

    # 2. metadata
    pages, compared, canonicals, posts = {}, 0, 0, 0
    for url, old in baseline.items():
        parser = PageParser()
        parser.feed(file_for(url).read_text(encoding="utf-8"))
        new = parser.result()
        pages[url] = parser
        for key, value in old.items():
            compared += 1
            if (new.get(key) or "").strip() != (value or "").strip():
                failures.append(f"{url} {key}: was {value!r}, now {new.get(key)!r}")
        canonicals += "canonical" in old
        posts += "datePublished" in old
    print(f"[2] metadata: {len(baseline)} pages, {compared} values compared, "
          f"{canonicals} canonicals, {posts} article dates")

    # 3. feeds
    xml_ids = [e.find(ATOM + "id").text for e in ET.parse(ROOT / "feed.xml").getroot().findall(ATOM + "entry")]
    json_urls = [item["url"] for item in json.loads((ROOT / "feed.json").read_text(encoding="utf-8"))["items"]]
    for name, now in (("feed.xml", xml_ids), ("feed.json", json_urls)):
        lost = [u for u in feeds[name] if u not in now]
        if lost:
            failures.append(f"{name} lost items: {lost}")
        for u in now:
            if not file_for(u.replace(SITE, "")).is_file():
                failures.append(f"{name} item has no page: {u}")
    print(f"[3] feeds: feed.xml {len(xml_ids)} entries, feed.json {len(json_urls)} items, "
          f"all {len(feeds['feed.xml'])} previous item URLs present")

    # 4. sitemap
    locs = [e.text for e in ET.parse(ROOT / "sitemap.xml").getroot().iter(SITEMAP + "loc")]
    lost = [u for u in feeds["sitemap.xml"] if u not in locs]
    if lost:
        failures.append(f"sitemap.xml lost URLs: {lost}")
    print(f"[4] sitemap: {len(locs)} URLs, all {len(feeds['sitemap.xml'])} previous URLs present")

    # 5. internal references from every built page
    broken, checked = set(), 0
    for url, parser in pages.items():
        for ref in parser.refs:
            if ref.startswith(SITE + "/"):
                ref = ref[len(SITE):]
            if not ref.startswith("/") or ref.startswith("//"):
                continue
            checked += 1
            if not file_for(ref.split("#")[0]).is_file():
                broken.add(f"{url} -> {ref}")
    failures += [f"broken link: {b}" for b in sorted(broken)]
    print(f"[5] internal links: {checked} checked across {len(pages)} pages, {len(broken)} broken")

    if failures:
        print(f"\nFAIL: {len(failures)} problem(s)")
        for f in failures:
            print("  " + f)
        sys.exit(1)
    print("\nOK: every inventoried URL, canonical, feed item and sitemap URL is intact")


if __name__ == "__main__":
    main()
