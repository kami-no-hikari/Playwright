from pages.base_page import BasePage


class TodoPage(BasePage):
    URL = "https://demo.playwright.dev/todomvc/#/"

    def __init__(self, page):
        super().__init__(page)
        self.new_todo_input = page.get_by_placeholder("What needs to be done?")

    def navigate(self):
        self.open(self.URL)

    def add_todo(self, text):
        self.new_todo_input.click()
        self.new_todo_input.fill(text)
        self.new_todo_input.press("Enter")

    def get_todo_item(self, text):
        return self.page.get_by_text(text)