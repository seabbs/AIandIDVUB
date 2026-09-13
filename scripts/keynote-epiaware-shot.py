#!/usr/bin/env -S uv run --with playwright --script
"""Screenshot the two approaches on epiaware.org/approaches.

Usage:
    ./scripts/keynote-epiaware-shot.py

Writes figures/keynote-epiaware-approaches.png, clipped to "The
approaches" section. Requires "uvx --from playwright playwright install
chromium" once, and network access.
"""

from pathlib import Path

from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
out = root / "figures" / "keynote-epiaware-approaches.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1500, "height": 1000},
                            device_scale_factor=2)
    page.goto("https://epiaware.org/approaches/")
    page.wait_for_load_state("load")
    page.wait_for_timeout(2000)
    head = page.query_selector("h2:has-text('The approaches')")
    head.scroll_into_view_if_needed()
    page.evaluate("window.scrollBy(0, -30)")
    page.wait_for_timeout(500)
    top = head.bounding_box()["y"] - 20
    cards = page.query_selector("text=More approaches may join these")
    bottom = cards.bounding_box()["y"] + 40
    page.screenshot(path=str(out),
                    clip={"x": 90, "y": top, "width": 1320,
                          "height": bottom - top})
    print("wrote", out.relative_to(root))
    browser.close()
