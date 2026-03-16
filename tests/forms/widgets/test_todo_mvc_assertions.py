from playwright.sync_api import expect


def test_todo_mvc_form_assertions(todo_mvc_page):
    todo_mvc_page.navigate()

    expect(
        todo_mvc_page.page,
        "Открыт некорректный URL страницы TodoMVC"
    ).to_have_url("https://demo.playwright.dev/todomvc/#/")

    expect(
        todo_mvc_page.get_input_field(),
        "Поле ввода задачи должно быть пустым"
    ).to_be_empty()

    todo_mvc_page.add_todo("Закончить курс по Playwright")
    todo_mvc_page.add_todo("Добавить в резюме, что умею автоматизировать")

    expect(
        todo_mvc_page.get_todo_items(),
        "Количество задач должно быть равно двум"
    ).to_have_count(2)

    todo_mvc_page.complete_todo_by_index(0)

    expect(
        todo_mvc_page.get_todo_item_by_index(0),
        "Первая задача должна быть отмечена выполненной"
    ).to_have_class("completed")