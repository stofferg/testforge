from playwright.sync_api import Page


class ExamplePage:
    def __init__(self, page: Page):
        self.page = page
        self.learn_more_link = page.get_by_role("link", name="Learn more")

    def open(self):
        self.page.goto("https://example.com")

    def click_learn_more(self):
        self.learn_more_link.click()