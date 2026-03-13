def test_dialogs(dialog_page):
    dialog_page.navigate()
    dialog_page.click_all_dialogs()

def test_ok_dialogs(dialog_page):
    dialog_page.navigate()
    dialog_page.ok_dialog_confirmation()