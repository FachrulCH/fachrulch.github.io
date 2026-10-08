#!/usr/bin/env python3
"""Migration check: does every built article say what the Publii page said?

    python3 tools/verify_content.py [slug ...]

For each post, compares the old article body (from git, SOURCE_REV) with the
new one: the visible text (whitespace-normalised), the image sources, the link
targets, the iframes/embeds and the number of code blocks. Prints one line
per post and the differences found. Needs beautifulsoup4 + lxml.
"""
import re
import sys

from bs4 import BeautifulSoup

from extract import ROOT, SITE, git_show, local_url


def norm_text(el):
    """Visible text with all whitespace removed: catches lost or changed words
    without tripping over how inline markup and line breaks were spaced."""
    for junk in el.select("script, style"):
        junk.decompose()
    return re.sub(r"\s+", "", el.get_text())


def code_texts(el):
    out = []
    for pre in el.find_all("pre"):
        for br in pre.find_all("br"):
            br.replace_with("\n")
        out.append("\n".join(line.rstrip() for line in pre.get_text().strip().split("\n")))
    return out


def norm_url(url):
    url = local_url(url or "").strip()
    return url.rstrip("/") or "/"


def facts(el):
    return {
        "img": sorted(norm_url(i.get("src")) for i in el.find_all("img")),
        "a": sorted(norm_url(a.get("href")) for a in el.find_all("a") if a.get("href")),
        "iframe": sorted(norm_url(f.get("src")) for f in el.find_all("iframe")),
        "script": sorted(norm_url(s.get("src")) for s in el.find_all("script") if s.get("src")),
        "pre": len(el.find_all("pre")),
    }


def compare(slug):
    old = BeautifulSoup(git_show(f"{slug}/index.html"), "lxml").select_one(".post__entry")
    new = BeautifulSoup((ROOT / slug / "index.html").read_text(encoding="utf-8"), "lxml").select_one(".prose")
    problems = []
    old_facts, new_facts = facts(old), facts(new)
    for key in old_facts:
        if old_facts[key] != new_facts[key]:
            if key == "pre":
                problems.append(f"code blocks {old_facts[key]} -> {new_facts[key]}")
            else:
                gone = [x for x in old_facts[key] if x not in new_facts[key]]
                added = [x for x in new_facts[key] if x not in old_facts[key]]
                problems.append(f"{key}: lost {gone} added {added}")
    for i, (x, y) in enumerate(zip(code_texts(old), code_texts(new))):
        if x != y:
            problems.append(f"code block {i + 1} differs: old {x[:120]!r} new {y[:120]!r}")
    a, b = norm_text(old), norm_text(new)
    if a != b:
        i = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        problems.append(f"text differs at char {i}: old …{a[max(0, i - 40):i + 40]!r} new …{b[max(0, i - 40):i + 40]!r}")
    return len(a), problems


def main():
    slugs = sys.argv[1:] or sorted(p.stem for p in (ROOT / "content/posts").glob("*.md"))
    bad = 0
    for slug in slugs:
        chars, problems = compare(slug)
        bad += bool(problems)
        print(f"{'OK  ' if not problems else 'DIFF'} {slug} ({chars} chars)")
        for p in problems:
            print("     " + p)
    print(f"\n{len(slugs) - bad}/{len(slugs)} posts identical in text, images, links, embeds and code blocks")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
