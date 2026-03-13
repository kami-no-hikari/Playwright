from pages.base_page import BasePage

class CheckboxPage(BasePage):
    URL = "https://zimaev.github.io/checks-radios/"

    def __init__(self, page):
        super().__init__(page)
        self.default_checkbox = page.get_by_text("Default checkbox")
        self.checked_checkbox = page.get_by_text("Checked checkbox")
        self.default_radio = page.get_by_text("Default radio")
        self.default_checked_radio = page.get_by_text("Default checked radio")
        self.checked_switch = page.get_by_text("Checked switch checkbox input")

    def navigate(self):
        self.open(self.URL)

    def check_all(self):
        self.default_checkbox.check()
        self.checked_checkbox.check()
        self.default_radio.check()
        self.default_checked_radio.check()
        self.checked_switch.check()

    def click_all(self):
        self.default_checkbox.click()
        self.checked_checkbox.click()
        self.default_radio.click()
        self.default_checked_radio.click()
        self.checked_switch.click()