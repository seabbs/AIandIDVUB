#!/usr/bin/env -S uv run --with playwright --script
"""Screenshot the live pages the communication deck shows as artefacts.

Usage:
    ./scripts/comms-shots.py

Writes figures/comms-shot-*.png. Requires
"uvx --from playwright playwright install chromium" once. Each entry is a
name, a URL, an optional CSS selector to scroll into view first, and an
optional extra scroll in pixels, so a long page can be shot at the part the
slide is about.
"""

from pathlib import Path

from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
out = root / "figures"

SHOTS = [
    (
        "spimo-statement",
        "https://www.gov.uk/government/publications/"
        "spi-m-o-consensus-statement-on-covid-19-17-september-2020",
        None,
    ),
    (
        "covid-issue-171",
        "https://github.com/epiforecasts/covid/issues/171",
        None,
    ),
    (
        "covid-uk",
        "https://epiforecasts.io/covid/posts/national/united-kingdom/",
        "#national-summary",
        900,
    ),
    ("epinowcast-forum", "https://community.epinowcast.org/", None),
    ("seabbs-bot", "https://github.com/seabbs-bot", None),
    (
        "juliacon-prompts",
        "https://samabbott.co.uk/JuliaCon2026/prompts.html",
        None,
    ),
    (
        "juliacon-steers",
        "https://samabbott.co.uk/JuliaCon2026/prompts.html#the-steers",
        "#the-steers",
    ),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 1440, "height": 1000}, device_scale_factor=1.5
    )
    for name, url, selector, *rest in SHOTS:
        scroll_by = rest[0] if rest else 0
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(2500)
            # GOV.UK puts a cookie banner over the page title.
            reject = page.get_by_role("button", name="Reject additional cookies")
            if reject.count():
                reject.first.click()
                page.wait_for_timeout(500)
                hide = page.get_by_role("button", name="Hide cookie message")
                if hide.count():
                    hide.first.click()
                    page.wait_for_timeout(300)
            if selector:
                page.locator(selector).first.scroll_into_view_if_needed()
                page.wait_for_timeout(600)
            if scroll_by:
                page.mouse.wheel(0, scroll_by)
                page.wait_for_timeout(600)
            path = out / f"comms-shot-{name}.png"
            page.screenshot(path=str(path))
            print(path)
        except Exception as exc:  # noqa: BLE001
            print(f"failed {name}: {exc}")
    browser.close()
