from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url

    def reload(self):
        self.page.reload()

    def go_back(self):
        self.page.go_back()

    def go_forward(self):
        self.page.go_forward()

    def screenshot(self, path: str):
        self.page.screenshot(path=path)