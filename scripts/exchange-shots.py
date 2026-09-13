#!/usr/bin/env -S uv run --with playwright --script
"""Screenshot every slide of a rendered revealjs deck at 1920 by 1080.

Usage:
    ./scripts/exchange-shots.py [deck] [outdir]

Like keynote-shots.py, but walks with Reveal.next() until the last slide
and its last fragment, so uncounted slides and fragments are shot too.
Reports any slide whose content box is taller than the viewport.
"""

import functools
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
site = root / "_site"
deck = sys.argv[1] if len(sys.argv) > 1 else "exchange"
outdir = Path(sys.argv[2]) if len(sys.argv) > 2 else root / "_shots" / deck
outdir.mkdir(parents=True, exist_ok=True)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass


handler = functools.partial(QuietHandler, directory=str(site))
server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
port = server.server_address[1]
threading.Thread(target=server.serve_forever, daemon=True).start()

HEIGHT_JS = (
    "(() => { const s = Reveal.getCurrentSlide();"
    " const r = s.getBoundingClientRect();"
    " let bottom = 0; s.querySelectorAll('*').forEach(e => {"
    "  const b = e.getBoundingClientRect();"
    "  if (b.height > 0) bottom = Math.max(bottom, b.bottom); });"
    " return Math.round(bottom - r.top); })()"
)
TITLE_JS = (
    "(() => { const s = Reveal.getCurrentSlide();"
    " const t = s.querySelector('h1, h2');"
    " return t ? t.innerText : ''; })()"
)

try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto(f"http://127.0.0.1:{port}/{deck}/slides.html")
        page.wait_for_load_state("load")
        page.wait_for_timeout(1500)
        i = 0
        while True:
            i += 1
            page.wait_for_timeout(350)
            idx = page.evaluate("Reveal.getIndices()")
            h, v, f = idx["h"], idx.get("v", 0), idx.get("f", -1)
            title = page.evaluate(TITLE_JS)
            height = page.evaluate(HEIGHT_JS)
            flag = "  OVERFLOW" if height > 1080 else ""
            frag = f" f={f}" if f is not None and f >= 0 else ""
            out = outdir / f"{i:02d}.png"
            page.screenshot(path=str(out))
            print(f"{i:02d} h={h} v={v}{frag} height={height}{flag}  {title}")
            done = page.evaluate(
                "Reveal.isLastSlide() && !Reveal.availableFragments().next")
            if done or i > 80:
                break
            page.evaluate("Reveal.next()")
        browser.close()
finally:
    server.shutdown()
    server.server_close()
