import re
from playwright.sync_api import expect


def test_example(page):
    page.goto("https://example.com")

    link = page.get_by_role("link", name="Learn more")

    expect(link).to_be_visible()

    link.click()

    expect(page).to_have_url("https://www.iana.org/help/example-domains")