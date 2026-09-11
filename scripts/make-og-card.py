#!/usr/bin/env -S uv run --with playwright --script
"""Render the Open Graph sharing card to figures/og-card.png at 1200x630.

Usage:
    ./scripts/make-og-card.py

The card is built as HTML and screenshotted, so it stays editable here rather
than living in a binary nobody can change. Requires
"uvx --from playwright playwright install chromium" once.
"""

import base64
from pathlib import Path

from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
out = root / "figures" / "og-card.png"

photo = base64.b64encode((root / "figures" / "sam.jpg").read_bytes()).decode()

TALKS = [
    ("09:00", "Keynote: Infectious disease modelling in the age of AI"),
    ("13:40", "Lecture: Science communication with and under AI"),
    ("15:20", "Panel: Where do we go next? AI, communication, collaboration"),
]

rows = "\n".join(
    f'<li><span class="t">{t}</span>{title}</li>' for t, title in TALKS
)

HTML = f"""
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 1200px; height: 630px;
    font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
    background: #ffffff;
    border-left: 18px solid #1f6f8b;
    padding: 58px 64px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}
  .top {{ display: flex; justify-content: space-between; }}
  h1 {{ font-size: 54px; letter-spacing: -1px; color: #1a1a1a; }}
  h2 {{
    font-size: 27px; font-weight: 400; color: #555;
    margin-top: 14px; max-width: 800px; line-height: 1.35;
  }}
  img {{
    width: 132px; height: 132px; border-radius: 10px;
    object-fit: cover; flex-shrink: 0;
  }}
  ul {{ list-style: none; }}
  li {{
    font-size: 25px; color: #222; padding: 9px 0;
    border-top: 1px solid #e3e3e3; line-height: 1.3;
  }}
  .t {{
    display: inline-block; width: 96px; color: #1f6f8b; font-weight: 700;
  }}
  .foot {{
    display: flex; justify-content: space-between;
    font-size: 23px; color: #666; border-top: 4px solid #4a5899;
    padding-top: 18px;
  }}
  .name {{ color: #1a1a1a; font-weight: 700; }}
</style>
<div class="top">
  <div>
    <h1>Combining infectious disease modelling and AI</h1>
    <h2>Two talks and a panel, VUB, Brussels</h2>
  </div>
  <img src="data:image/jpeg;base64,{photo}" alt="Sam Abbott">
</div>
<ul>{rows}</ul>
<div class="foot">
  <span><span class="name">Sam Abbott</span> · LSHTM</span>
  <span>Monday 14 September 2026 · Learning Theatre, VUB Etterbeek</span>
</div>
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 630})
    page.set_content(HTML)
    page.wait_for_timeout(300)
    page.screenshot(path=str(out))
    browser.close()

print(out)
