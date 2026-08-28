from playwright.sync_api import expect
from pages.example_page import ExamplePage


def test_learn_more_link_is_visible(page):
    example = ExamplePage(page)
    example.open()

    expect(example.learn_more_link).to_be_visible()


def test_learn_more_link_navigates_to_iana(page):
    example = ExamplePage(page)
    example.open()

    example.click_learn_more()

    expect(page).to_have_url(
        "https://www.iana.org/help/example-domains"
    )