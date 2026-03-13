from pages.base_page import BasePage

class DialogPage(BasePage):
    URL = "https://zimaev.github.io/dialog/"

    def __init__(self, page):
        super().__init__(page)
        self.dialog_alert = page.get_by_text("Диалог Alert")
        self.dialog_confirmation = page.get_by_text("Диалог Confirmation")
        self.dialog_prompt = page.get_by_text("Диалог Prompt")


    def navigate(self):
        self.open(self.URL)

    def click_all_dialogs(self):
        self.dialog_alert.click()
        self.dialog_confirmation.click()
        self.dialog_prompt.click()

    def ok_dialog_confirmation(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.dialog_confirmation.click()

