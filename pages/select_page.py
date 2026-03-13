from pages.base_page import BasePage


class SelectPage(BasePage):
    URL = "https://zimaev.github.io/select/"

    def __init__(self, page):
        super().__init__(page)
        self.single_select = page.locator("#floatingSelect")
        self.multi_select = page.locator("#skills")

    def navigate(self):
        self.open(self.URL)

    def select_by_value(self, value):
        self.single_select.select_option(value=value)

    def select_by_index(self, index):
        self.single_select.select_option(index=index)

    def select_by_label(self, label):
        self.single_select.select_option(label=label)

    def select_multiple(self, values):
        self.multi_select.select_option(values)