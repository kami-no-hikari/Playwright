"""locator.check(**kwargs) метод playwright созданный специально для работы с чекбоксами и радио кнопками."""
def test_checkbox_check_method(checkbox_page):
    checkbox_page.navigate()
    checkbox_page.check_all()

"""locator.click(**kwargs) обычный клик"""
def test_checkbox_click_method(checkbox_page):
    checkbox_page.navigate()
    checkbox_page.click_all()