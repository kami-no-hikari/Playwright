from pages.base_page import BasePage


class TodoMvcPage(BasePage):
    URL = "https://demo.playwright.dev/todomvc/#/"

    def __init__(self, page):
        super().__init__(page)
        self.input_field = page.get_by_placeholder("What needs to be done?")
        self.todo_items = page.get_by_test_id("todo-item")

    def navigate(self):
        self.open(self.URL)

    def add_todo(self, text):
        self.input_field.fill(text)
        self.input_field.press("Enter")

    def complete_todo_by_index(self, index):
        self.todo_items.get_by_role("checkbox").nth(index).click()

    def get_input_field(self):
        return self.input_field

    def get_todo_items(self):
        return self.todo_items

    def get_todo_item_by_index(self, index):
        return self.todo_items.nth(index)