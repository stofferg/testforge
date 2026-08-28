import pytest


@pytest.fixture
def example_page(page):
    page.goto("https://example.com")
    return page