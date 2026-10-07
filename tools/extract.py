#!/usr/bin/env python3
"""One-time migration: turn the Publii-generated HTML into content/ markdown.

    python3 tools/extract.py

Reads the pages from the last Publii commit (SOURCE_REV) through git, so it
still works after the build has overwritten the HTML in the working tree.
Writes content/posts/<slug>.md and content/tags.toml.

Simple blocks (paragraphs, headings, lists, quotes, code) become markdown.
Anything that does not map cleanly (figures, galleries, tables, embeds,
pasted Medium/Substack markup) is kept as raw HTML inside the markdown so
nothing is dropped. Needs beautifulsoup4 + lxml (migration only).
"""
import json
import re
import subprocess
from pathlib import Path

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent
SOURCE_REV = "68da9a3"  # last commit served from the Publii export
SITE = "https://fachrul.id"
TZ = "+04:00"  # Publii rendered every timestamp in Dubai time
DEFAULT_OG_IMAGE = "/media/website/profile-newletter-3.png"
NOT_POSTS = {"page", "celoteh", "authors", "assets", "media", "sdet", "tools"}

# Paragraph/heading classes that carry meaning in the old theme; others are
# leftovers from pasting (Medium "graf", Substack ids...) and are dropped.
KEPT_CLASSES = {"msg", "msg--info", "msg--highlight", "msg--warning", "msg--success",
                "dropcap", "align-center", "align-right"}
INLINE_MD = {"strong": "**", "b": "**", "em": "*", "i": "*"}
INLINE_RAW = {"u", "sub", "sup", "s", "del", "mark", "small", "kbd", "abbr", "time", "q", "cite"}


def git_show(path):
    return subprocess.run(["git", "show", f"{SOURCE_REV}:{path}"], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout


def git_paths():
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", SOURCE_REV], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
    return out.splitlines()


def local_url(url):
    """https://fachrul.id/x -> /x so pages work on a local preview too."""
    if url and (url == SITE or url.startswith(SITE + "/")):
        return url[len(SITE):] or "/"
    return url


def relink(tag):
    for el in [tag] + tag.find_all(True):
        for attr in ("href", "src", "data-src"):
            if el.get(attr):
                el[attr] = local_url(el[attr])
        for attr in ("srcset",):
            if el.get(attr):
                el[attr] = el[attr].replace(SITE + "/", "/")
    return tag


def escape_text(text):
    text = text.replace("\\", "\\\\")
    for ch in "`*_[]":
        text = text.replace(ch, "\\" + ch)
    return text.replace("&", "&amp;").replace("<", "&lt;")


def escape_line_start(md):
    md = re.sub(r"^(#|>|=)", r"\\\1", md)
    md = re.sub(r"^([-+*]) ", r"\\\1 ", md)
    return re.sub(r"^(\d+)([.)]) ", r"\1\\\2 ", md)


class Unclean(Exception):
    """Raised when an element cannot be expressed as plain markdown."""


def inline(node):
    if isinstance(node, Comment):
        return ""
    if isinstance(node, NavigableString):
        return escape_text(re.sub(r"[ \t\r\n]+", " ", str(node)))
    name = node.name
    if name == "br":
        return "<br>"
    if name == "span" or name == "font":
        return "".join(inline(c) for c in node.children)
    if name in INLINE_MD:
        inner = "".join(inline(c) for c in node.children)
        if not inner.strip():
            return inner
        mark = INLINE_MD[name]
        lead = inner[: len(inner) - len(inner.lstrip())]
        trail = inner[len(inner.rstrip()):]
        return f"{lead}{mark}{inner.strip()}{mark}{trail}"
    if name == "code":
        text = node.get_text()
        if not text:
            return ""
        fence = "``" if "`" in text else "`"
        pad = " " if text.startswith("`") or text.endswith("`") else ""
        return f"{fence}{pad}{text}{pad}{fence}"
    if name == "a" and node.get("href"):
        href = local_url(node["href"])
        text = "".join(inline(c) for c in node.children)
        if re.search(r"[\s()<>]", href) or not text.strip():
            return str(relink(node))
        title = node.get("title")
        if title and '"' not in title:
            return f'[{text}]({href} "{title}")'
        return f"[{text}]({href})"
    if name == "img" and node.get("src") and not node.get("srcset"):
        alt = escape_text(node.get("alt", ""))
        return f"![{alt}]({local_url(node['src'])})"
    if name in INLINE_RAW or name in ("a", "img", "iframe", "input", "label"):
        return str(relink(node))
    raise Unclean(name)


def inline_block(node):
    md = "".join(inline(c) for c in node.children)
    md = re.sub(r" {2,}", " ", md).strip()
    return escape_line_start(md)


def attr_suffix(node):
    classes = [c for c in node.get("class", []) if c in KEPT_CLASSES]
    parts = [f"#{node['id']}"] if node.get("id") and node.name.startswith("h") and not re.search(r"\s", node["id"]) else []
    parts += [f".{c}" for c in classes]
    return f" {{: {' '.join(parts)} }}" if parts else ""


def code_block(pre):
    lang = ""
    for el in [pre] + pre.find_all(True):
        lang = next((c[len("language-"):] for c in el.get("class", []) if c.startswith("language-")), "")
        if lang:
            break
    for br in pre.find_all("br"):
        br.replace_with("\n")
    text = pre.get_text().strip("\n")
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}{lang}\n{text}\n{fence}"


def list_block(node, depth=0):
    items = []
    for i, li in enumerate(node.find_all("li", recursive=False)):
        marker = f"{i + 1}." if node.name == "ol" else "-"
        parts, current = [], []
        for child in li.children:
            if isinstance(child, Tag) and child.name in ("ul", "ol"):
                if current:
                    parts.append(("inline", current))
                    current = []
                parts.append(("list", child))
            elif isinstance(child, Tag) and child.name == "p":
                if current:
                    parts.append(("inline", current))
                    current = []
                parts.append(("inline", list(child.children)))
            elif isinstance(child, Tag) and child.name in ("div", "pre", "figure", "table", "blockquote", "h1", "h2", "h3", "h4"):
                raise Unclean("li>" + child.name)
            else:
                current.append(child)
        if current:
            parts.append(("inline", current))
        rendered = []
        for kind, value in parts:
            if kind == "list":
                rendered.append((kind, list_block(value, depth + 1)))
            else:
                text = re.sub(r" {2,}", " ", "".join(inline(c) for c in value)).strip()
                if text:
                    rendered.append((kind, escape_line_start(text)))
        if not rendered or rendered[0][0] == "list":
            rendered.insert(0, ("inline", ""))
        body = f"{marker} {rendered[0][1]}".rstrip()
        for kind, text in rendered[1:]:
            text = "\n".join("    " + line if line else line for line in text.split("\n"))
            # A nested list directly under the item text needs no blank line;
            # a second paragraph does.
            body += ("\n" if kind == "list" else "\n\n") + text
        items.append(body)
    return "\n".join(items)


def blockquote_block(node):
    if node.get("class") or node.get("style") or node.find(["script", "iframe", "figure", "table", "div"]):
        raise Unclean("blockquote")
    inner = convert_children(node)
    return "\n".join("> " + line if line else ">" for line in inner.split("\n"))


def block(node):
    if isinstance(node, Comment):
        return ""
    if isinstance(node, NavigableString):
        text = escape_text(re.sub(r"\s+", " ", str(node))).strip()
        return escape_line_start(text)
    name = node.name
    try:
        if name == "p":
            if node.find(["div", "figure", "table", "pre", "ul", "ol", "iframe", "script"]):
                raise Unclean("p>block")
            md = inline_block(node)
            if not md or md == "<br>" or not node.get_text(strip=True) and not node.find("img"):
                return ""
            return md + ("\n" + attr_suffix(node).strip() if attr_suffix(node) else "")
        if re.fullmatch(r"h[1-6]", name):
            if node.find(["div", "figure", "img", "br"]):
                raise Unclean("heading")
            md = inline_block(node)
            if not md:
                return ""
            return "#" * int(name[1]) + " " + md + attr_suffix(node)
        if name in ("ul", "ol"):
            if node.get("start") or node.get("class") or node.get("type"):
                raise Unclean(name)
            return list_block(node)
        if name == "pre":
            return code_block(node)
        if name == "hr":
            return "---"
        if name == "br":
            return ""
        if name == "blockquote":
            return blockquote_block(node)
    except Unclean:
        pass
    return str(relink(node))


def convert_children(node):
    blocks = [block(c) for c in node.children]
    return "\n\n".join(b for b in blocks if b.strip())


def clean_body(entry):
    # Publii editor leftovers: inline styles copying theme variables.
    for span in entry.find_all("span", style=re.compile(r"var\(--")):
        span.unwrap()
    for el in entry.find_all(style=re.compile(r"^\s*$")):
        del el["style"]
    # Gallery thumbnails are links whose only content is an image without alt
    # text; give the image its caption so the link has an accessible name.
    for item in entry.select("figure.gallery__item"):
        img, caption = item.find("img"), item.find("figcaption")
        if img is not None and not img.get("alt") and caption is not None:
            img["alt"] = caption.get_text(strip=True)
    return entry


def toml_str(value):
    return json.dumps(value, ensure_ascii=False)


def iso(stamp, seconds="00"):
    """2024-01-01T20:19 -> 2024-01-01T20:19:00+04:00"""
    return f"{stamp}:{seconds}{TZ}" if len(stamp) == 16 else stamp


def extract_post(slug, html, sitemap_lastmod, listed, tag_slugs):
    soup = BeautifulSoup(html, "lxml")
    meta = {m.get("name") or m.get("property"): m.get("content") for m in soup.find_all("meta")}
    ld = next(json.loads(s.string) for s in soup.find_all("script", type="application/ld+json")
              if json.loads(s.string).get("@type") == "Article")
    title = soup.find("h1").get_text(strip=True)
    canonical = soup.find("link", rel="canonical")["href"]
    updated = sitemap_lastmod.get(slug) or iso(ld["dateModified"])
    # Seconds are only known through the sitemap; reuse them when unedited.
    date = updated if ld["datePublished"] == ld["dateModified"] else iso(ld["datePublished"])

    fm = [("title", title)]
    if soup.title.get_text() != f"{title} - Fachrul Choliluddin":
        fm.append(("seo_title", soup.title.get_text()))
    fm.append(("date", date))
    fm.append(("updated", updated))
    tags = [tag_slugs[a.get_text()] for a in soup.select(".post__tag a")]
    fm.append(("tags", tags))
    fm.append(("description", meta.get("description", "")))

    hero = soup.select_one("figure.hero__image img")
    cover = local_url(hero["src"]) if hero else ""
    if hero:
        fm.append(("cover", cover))
        if hero.get("alt"):
            fm.append(("cover_alt", hero["alt"]))
        caption = soup.select_one("figure.hero__image figcaption")
        if caption and caption.get_text(strip=True):
            fm.append(("cover_caption", caption.decode_contents().strip()))
    og_image = local_url(meta["og:image"])
    if og_image != (cover or DEFAULT_OG_IMAGE):
        fm.append(("og_image", og_image))
    if meta["og:title"] != title:
        fm.append(("og_title", meta["og:title"]))
    if canonical != f"{SITE}/{slug}/":
        fm.append(("canonical", canonical))
    if not listed:
        fm.append(("listed", False))

    lines = ["+++"]
    for key, value in fm:
        if key in ("date", "updated"):
            lines.append(f"{key} = {value}")
        elif isinstance(value, bool):
            lines.append(f"{key} = {'true' if value else 'false'}")
        elif isinstance(value, list):
            lines.append(f"{key} = [{', '.join(toml_str(v) for v in value)}]")
        else:
            lines.append(f"{key} = {toml_str(value)}")
    lines.append("+++")
    body = convert_children(clean_body(soup.select_one(".post__entry")))
    return "\n".join(lines) + "\n\n" + body + "\n"


def tag_index():
    """Display name, slug and description of every tag, from /celoteh/."""
    soup = BeautifulSoup(git_show("celoteh/index.html"), "lxml")
    tags = []
    for item in soup.select("main li"):
        link = item.find("a", href=re.compile(r"/celoteh/[^/]+/$"))
        if not link:
            continue
        slug = link["href"].rstrip("/").rsplit("/", 1)[1]
        if any(t["slug"] == slug for t in tags):
            continue
        tag_page = BeautifulSoup(git_show(f"celoteh/{slug}/index.html"), "lxml")
        heading = tag_page.select_one("main h1")
        for count in heading.find_all("sup"):
            count.decompose()
        name = heading.get_text(strip=True)
        desc_el = tag_page.select_one("main .page__desc")
        og_desc = tag_page.find("meta", property="og:description")["content"]
        tags.append({"slug": slug, "name": name, "description": desc_el.get_text(strip=True) if desc_el else "",
                     "og_description": og_desc})
    return tags


def main():
    paths = git_paths()
    slugs = sorted(p.split("/")[0] for p in paths
                   if re.fullmatch(r"[^/]+/index\.html", p) and p.split("/")[0] not in NOT_POSTS)
    sitemap = git_show("sitemap.xml")
    lastmod = {u.strip("/"): lm for u, lm in
               re.findall(r"<loc>https://fachrul.id(/[^<]*)</loc>\s*<lastmod>([^<]*)</lastmod>", sitemap)}
    listed = set()
    for p in paths:
        if re.fullmatch(r"authors/fachrulch/(page/\d+/)?index\.html", p):
            soup = BeautifulSoup(git_show(p), "lxml")
            for art in soup.select("main article"):
                for a in art.select("a[href]"):
                    m = re.fullmatch(re.escape(SITE) + r"/([^/]+)/", a["href"])
                    if m and m.group(1) not in NOT_POSTS:
                        listed.add(m.group(1))
                        break

    tags = tag_index()
    tag_slugs = {t["name"]: t["slug"] for t in tags}
    out = ["# Tags: the URL is /celoteh/<slug>/. Posts list tags by slug.",
           "# description is shown on the tag page; og_description goes to link previews.", ""]
    for t in tags:
        out += [f"[{toml_str(t['slug'])}]", f"name = {toml_str(t['name'])}",
                f"description = {toml_str(t['description'])}",
                f"og_description = {toml_str(t['og_description'])}", ""]
    (ROOT / "content").mkdir(exist_ok=True)
    (ROOT / "content/tags.toml").write_text("\n".join(out), encoding="utf-8")

    posts_dir = ROOT / "content/posts"
    posts_dir.mkdir(parents=True, exist_ok=True)
    for slug in slugs:
        md = extract_post(slug, git_show(f"{slug}/index.html"), lastmod, slug in listed, tag_slugs)
        (posts_dir / f"{slug}.md").write_text(md, encoding="utf-8")
    print(f"{len(slugs)} posts ({len(listed)} listed), {len(tags)} tags")


if __name__ == "__main__":
    main()
