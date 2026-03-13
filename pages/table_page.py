from pages.base_page import BasePage


class TablePage(BasePage):
    URL = "https://zimaev.github.io/table/"

    def __init__(self, page):
        super().__init__(page)
        self.rows_source = page.locator("tr")

    def open_page(self):
        self.page.goto(self.URL)

    def get_all_inner_texts(self):
        return self.rows_source.all_inner_texts()