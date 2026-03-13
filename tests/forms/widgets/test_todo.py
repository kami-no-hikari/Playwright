
def test_add_todo(todo_page):
    todo_page.navigate()
    todo_page.add_todo("Создать первый сценарий playwright")

    assert todo_page.get_todo_item("Создать первый сценарий playwright").is_visible()