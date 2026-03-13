from pages.base_page import BasePage
class DragAndDrop(BasePage):
    URL = "https://zimaev.github.io/draganddrop/"

    def __init__(self, page):
        super().__init__(page)
        self.drag_source = "#drag"
        self.drop_target = "#drop"


    def drag_drop(self):
        self.page.drag_and_drop(self.drag_source, self.drop_target)

    def navigate(self):
        self.open(self.URL)

