from pages.base_page import BasePage


class ApplitoolsPage(BasePage):
    URL = "https://demo.applitools.com/"

    def __init__(self, page):
        super().__init__(page)
        self.form = page.locator("form")

    def open_page(self):
        self.page.goto(self.URL)

    def make_page_screenshot(self):
        self.page.screenshot(path="screenshots/page.png")

    def make_full_page_screenshot(self):
        self.page.screenshot(path="screenshots/full_page.png", full_page=True)

    def make_form_screenshot(self):
        self.form.screenshot(path="screenshots/form.png")