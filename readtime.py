#!/usr/bin/env python3
"""Stamp an estimated reading time next to each write-up link.

Usage:  python3 readtime.py

For every write-up in writeups/, counts the words inside Quarto's
<main id="quarto-document-content">, then rewrites any element like

    <span class="readtime" data-src="../writeups/foo.html">…</span>

in the hand-written pages (data-src is relative to the page) so its text reads "N min read".

Estimate: prose at 230 wpm, code at 1/3 that speed (people skim it,
but slowly), plus 12 s per image/figure. Rounded up, minimum 1 min.
Standard library only.
"""

import math
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ["pages/landing.html", "pages/writeups.html"]

WPM = 230
CODE_SLOWDOWN = 3
SECONDS_PER_IMAGE = 12

SKIP = {"script", "style", "svg", "noscript", "button"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "source", "track", "wbr"}


class Counter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []          # open tags inside <main>
        self.in_main = False
        self.skip = 0
        self.code = 0
        self.prose_words = 0
        self.code_words = 0
        self.images = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if not self.in_main:
            if tag == "main" and a.get("id") == "quarto-document-content":
                self.in_main = True
                self.stack = ["main"]
            return
        if tag == "img":
            self.images += 1
        if tag in VOID:
            return
        self.stack.append(tag)
        if tag in SKIP:
            self.skip += 1
        if tag == "pre":
            self.code += 1

    def handle_endtag(self, tag):
        if not self.in_main or tag in VOID or tag not in self.stack:
            return
        while self.stack:
            t = self.stack.pop()
            if t in SKIP:
                self.skip -= 1
            if t == "pre":
                self.code -= 1
            if t == tag:
                break
        if not self.stack:
            self.in_main = False

    def handle_data(self, data):
        if not self.in_main or self.skip:
            return
        n = len(re.findall(r"\w+", data))
        if self.code:
            self.code_words += n
        else:
            self.prose_words += n


def minutes(path: Path) -> tuple[int, Counter]:
    c = Counter()
    c.feed(path.read_text(encoding="utf-8"))
    secs = (c.prose_words / WPM * 60
            + c.code_words * CODE_SLOWDOWN / WPM * 60
            + c.images * SECONDS_PER_IMAGE)
    return max(1, math.ceil(secs / 60)), c


SPAN = re.compile(
    r'(<span class="readtime" data-src="([^"]+)">)(.*?)(</span>)', re.S)


def main():
    cache = {}

    def stamp(m, page_dir):
        src = (page_dir / m.group(2)).resolve()
        if src not in cache:
            mins, c = minutes(src)
            cache[src] = mins
            print(f"{src.relative_to(ROOT)}: {c.prose_words} prose + {c.code_words} code words, "
                  f"{c.images} images -> {mins} min")
        return f"{m.group(1)}{cache[src]} min read{m.group(4)}"

    for page in PAGES:
        p = ROOT / page
        text = p.read_text(encoding="utf-8")
        new = SPAN.sub(lambda m: stamp(m, p.parent), text)
        if new != text:
            p.write_text(new, encoding="utf-8")
            print(f"updated {page}")


if __name__ == "__main__":
    main()
