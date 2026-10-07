#!/usr/bin/env python3
"""Build fachrul.id: content/ + templates/ -> HTML at the repo root.

    python3 tools/build.py

GitHub Pages serves the repo root of master, so every page is written to the
same path the old Publii export used (/<slug>/index.html, /celoteh/<tag>/,
/page/N/ ...). Run tools/check_urls.py afterwards.
"""
import html
import json
import math
import re
import struct
import tomllib
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader
from pygments.formatters import HtmlFormatter

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
RESPONSIVE_SIZES = [("xs", 300), ("sm", 480), ("md", 768), ("lg", 1024), ("xl", 1360), ("2xl", 1600)]


# --- content -----------------------------------------------------------------

def read_post(path, site):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\+\+\+\n(.*?)\n\+\+\+\n", text, re.S)
    if not match:
        raise SystemExit(f"{path}: missing +++ front matter")
    meta = tomllib.loads(match.group(1))
    for key in ("title", "date"):
        if key not in meta:
            raise SystemExit(f"{path}: front matter needs '{key}'")
    md = markdown.Markdown(
        extensions=["fenced_code", "codehilite", "attr_list", "tables"],
        extension_configs={"codehilite": {"guess_lang": False, "css_class": "highlight"}},
    )
    body = md.convert(text[match.end():])
    prose = re.sub(r"<pre.*?</pre>", " ", body, flags=re.S)
    prose = re.sub(r"</(p|li|h\d|div|td|figcaption|blockquote)>|<br ?/?>", " ", prose)
    plain = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", prose))).strip()
    words = plain.split(" ")
    slug = meta.get("slug", path.stem)
    date = meta["date"]
    updated = meta.get("updated", date)
    cover = meta.get("cover", "")
    return {
        **meta,
        "slug": slug,
        "url": f"/{slug}/",
        "date": date,
        "updated": updated,
        "tags": meta.get("tags", []),
        "listed": meta.get("listed", True),
        "description": meta.get("description") or " ".join(words[:50]) + "…",
        "cover": cover,
        "og_image": meta.get("og_image") or cover or site["image"],
        "canonical": meta.get("canonical", f"{site['url']}/{slug}/"),
        "body": body,
        "has_code": 'class="highlight"' in body,
        "reading_minutes": max(1, round(len(words) / 200)),
    }


def load():
    site = tomllib.loads((CONTENT / "site.toml").read_text(encoding="utf-8"))
    tags = tomllib.loads((CONTENT / "tags.toml").read_text(encoding="utf-8"))
    posts = [read_post(p, site) for p in sorted((CONTENT / "posts").glob("*.md"))]
    posts.sort(key=lambda p: p["date"], reverse=True)
    for post in posts:
        post["tag_list"] = []
        for slug in post["tags"]:
            tags.setdefault(slug, {"name": slug, "description": ""})
            post["tag_list"].append({"slug": slug, "name": tags[slug]["name"]})
    return site, tags, posts


# --- helpers -------------------------------------------------------------------

def image_size(path):
    """(width, height) of a PNG/JPEG/GIF/WebP file, or None."""
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return struct.unpack("<HH", data[6:10])
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        if data[12:16] == b"VP8X":
            return (int.from_bytes(data[24:27], "little") + 1, int.from_bytes(data[27:30], "little") + 1)
        if data[12:16] == b"VP8 ":
            w, h = struct.unpack("<HH", data[26:30])
            return (w & 0x3FFF, h & 0x3FFF)
    if data[:2] == b"\xff\xd8":
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return (w, h)
            i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return None


def srcset(url):
    """Publii stored resized copies next to each image under responsive/."""
    path = Path(url)
    variants = []
    for name, width in RESPONSIVE_SIZES:
        candidate = f"{path.parent}/responsive/{path.stem}-{name}{path.suffix}"
        if (ROOT / candidate.lstrip("/")).is_file():
            variants.append(f"{candidate} {width}w")
    return ", ".join(variants)


def short_date(value):
    return f"{value.day} {MONTHS[value.month - 1]} {value.year}"


def minute_stamp(value):
    return value.strftime("%Y-%m-%dT%H:%M")


def absolute(site, fragment):
    """Root-relative links -> absolute ones, for feeds."""
    return re.sub(r'(href|src)="/(?!/)', rf'\1="{site["url"]}/', fragment).replace(
        ' srcset="/', f' srcset="{site["url"]}/').replace(', /media/', f', {site["url"]}/media/')


def paginate(items, per_page):
    pages = max(1, math.ceil(len(items) / per_page))
    return [items[i * per_page:(i + 1) * per_page] for i in range(pages)]


def page_url(base, number):
    return base if number == 1 else f"{base}page/{number}/"


# --- writers -------------------------------------------------------------------

class Builder:
    def __init__(self):
        self.site, self.tags, self.posts = load()
        self.listed = [p for p in self.posts if p["listed"]]
        self.env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=True,
                               trim_blocks=True, lstrip_blocks=True)
        self.env.filters["short_date"] = short_date
        self.env.filters["minute_stamp"] = minute_stamp
        self.env.filters["srcset"] = srcset
        self.css = (TEMPLATES / "site.css").read_text(encoding="utf-8")
        self.code_css = HtmlFormatter(style="github-dark").get_style_defs(".highlight")
        self.written = []

    def write(self, rel_path, text):
        path = ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        self.written.append(rel_path)

    def og(self, url, title, description, image=None, og_type="website"):
        image = image or self.site["image"]
        size = image_size(ROOT / image.lstrip("/")) if image.startswith("/") else None
        return {"url": self.site["url"] + url, "title": title, "description": description,
                "image": self.site["url"] + image if image.startswith("/") else image,
                "width": size[0] if size else None, "height": size[1] if size else None,
                "type": og_type}

    def render(self, rel_path, template, **ctx):
        ctx.setdefault("css", self.css)
        ctx.setdefault("robots", None)
        ctx.setdefault("canonical", None)
        ctx.setdefault("description", None)
        self.write(rel_path, self.env.get_template(template).render(site=self.site, **ctx))

    def organization_ld(self):
        return json.dumps({
            "@context": "http://schema.org", "@type": "Organization", "name": self.site["title"],
            "logo": self.site["url"] + self.site["image"], "url": self.site["url"] + "/",
            "sameAs": [s["url"] for s in self.site["social"]],
        }, ensure_ascii=False)

    def article_ld(self, post, og):
        author = self.site["author"]
        image = {"@type": "ImageObject", "url": og["image"]}
        if og["width"]:
            image.update(height=og["height"], width=og["width"])
        logo = self.og("/", "", "")
        return json.dumps({
            "@context": "http://schema.org", "@type": "Article",
            "mainEntityOfPage": {"@type": "WebPage", "@id": post["canonical"]},
            "headline": post["title"],
            "datePublished": minute_stamp(post["date"]), "dateModified": minute_stamp(post["updated"]),
            "image": image, "description": post["description"],
            "author": {"@type": "Person", "name": author["name"],
                       "url": f"{self.site['url']}/authors/{author['slug']}/"},
            "publisher": {"@type": "Organization", "name": author["name"],
                          "logo": {"@type": "ImageObject", "url": logo["image"],
                                   "height": logo["height"], "width": logo["width"]}},
        }, ensure_ascii=False)

    def build_posts(self):
        for post in self.posts:
            neighbours = {}
            if post["listed"]:
                i = self.listed.index(post)
                neighbours["newer"] = self.listed[i - 1] if i > 0 else None
                neighbours["older"] = self.listed[i + 1] if i + 1 < len(self.listed) else None
            og = self.og(post["url"], post.get("og_title", post["title"]), post["description"],
                         post["og_image"], "article")
            css = self.css + (self.code_css if post["has_code"] else "")
            cover_size = image_size(ROOT / post["cover"].lstrip("/")) if post["cover"].startswith("/") else None
            self.render(f"{post['slug']}/index.html", "post.html", post=post, og=og, css=css,
                        title=post.get("seo_title", f"{post['title']} - {self.site['author']['name']}"),
                        description=post["description"], canonical=post["canonical"],
                        cover_size=cover_size, json_ld=self.article_ld(post, og),
                        archive=self.listed if post.get("archive") else None, **neighbours)

    def build_list(self, base, posts, per_page, title, og_title, og_description, self_canonical=False, **ctx):
        pages = paginate(posts, per_page)
        for number, chunk in enumerate(pages, 1):
            url = page_url(base, number)
            if self_canonical:
                ctx["canonical"] = self.site["url"] + url
            self.render(url.lstrip("/") + "index.html", "list.html", posts=chunk, title=title,
                        og=self.og(url, og_title, og_description), json_ld=self.organization_ld(),
                        newer=page_url(base, number - 1) if number > 1 else None,
                        older=page_url(base, number + 1) if number < len(pages) else None,
                        page_number=number, page_count=len(pages), **ctx)

    def build_lists(self):
        site = self.site
        self.build_list("/", self.listed, site["per_page_home"], site["title"], site["title"],
                        site["description"], kind="home", self_canonical=True,
                        description=site["description"])
        for slug, tag in self.tags.items():
            tagged = [p for p in self.listed if slug in p["tags"]]
            self.build_list(f"/celoteh/{slug}/", tagged, site["per_page_tag"],
                            f"Tag: {tag['name']} - {site['title']}", tag["name"],
                            tag.get("og_description") or tag["description"] or site["description"],
                            kind="tag", tag=tag,
                            total=len(tagged), robots="noindex, follow")
        author = site["author"]
        self.build_list(f"/authors/{author['slug']}/", self.listed, site["per_page_author"],
                        f"Author: {author['name']} - {site['title']}", author["name"],
                        author["meta_description"], kind="author", total=len(self.listed),
                        robots="noindex, follow")
        counts = {slug: sum(slug in p["tags"] for p in self.listed) for slug in self.tags}
        self.render("celoteh/index.html", "tags.html", tags=self.tags, counts=counts,
                    title=f"All tags - {site['title']}", robots="noindex, follow",
                    og=self.og("/celoteh/", site["title"], site["description"]))
        home_og = self.og("/", site["title"], site["description"])
        self.render("search.html", "search.html", title=f"Search - {site['title']}",
                    robots="noindex, follow", og=home_og)
        self.render("404.html", "404.html", title=f"Error 404 - {site['title']}",
                    robots="noindex, follow", og=home_og, posts=self.listed[:5])

    def build_feeds(self):
        site = self.site
        items = self.listed[:site["feed_items"]]
        for post in items:
            post["feed_body"] = absolute(site, post["body"])
        self.write("feed.xml", self.env.get_template("feed.xml").render(
            site=site, posts=items, updated=max(p["updated"] for p in self.posts)))
        feed = {
            "version": "https://jsonfeed.org/version/1", "title": site["title"], "description": "",
            "home_page_url": site["url"], "feed_url": f"{site['url']}/feed.json", "user_comment": "",
            "icon": site["url"] + site["image"], "author": {"name": site["author"]["name"]},
            "items": [{
                "id": site["url"] + p["url"], "url": site["url"] + p["url"], "title": p["title"],
                "summary": p["description"], "content_html": p["feed_body"],
                "author": {"name": site["author"]["name"]}, "tags": [t["name"] for t in p["tag_list"]],
                "date_published": p["date"].isoformat(), "date_modified": p["updated"].isoformat(),
            } for p in items],
        }
        self.write("feed.json", json.dumps(feed, indent=4, ensure_ascii=False) + "\n")

    def build_sitemap(self):
        entries = [{"loc": "/", "lastmod": None, "images": []}]
        for post in sorted(self.posts, key=lambda p: p["slug"]):
            images = re.findall(r'<img[^>]+src="(/[^"]+)"', post["body"])
            if post["cover"]:
                images.insert(0, post["cover"])
            entries.append({"loc": post["url"], "lastmod": post["updated"].isoformat(),
                            "images": list(dict.fromkeys(images))})
        for number in range(2, len(paginate(self.listed, self.site["per_page_home"])) + 1):
            entries.append({"loc": page_url("/", number), "lastmod": None, "images": []})
        self.write("sitemap.xml", self.env.get_template("sitemap.xml").render(site=self.site, entries=entries))

    def run(self):
        self.build_posts()
        self.build_lists()
        self.build_feeds()
        self.build_sitemap()
        print(f"built {len(self.written)} files from {len(self.posts)} posts "
              f"({len(self.listed)} listed) and {len(self.tags)} tags")


if __name__ == "__main__":
    Builder().run()
