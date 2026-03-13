# Playwright UI Automation Framework

![CI](https://github.com/kami-no-hikari/Playwright/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Testing-orange)
![Framework](https://img.shields.io/badge/Test%20Framework-POM-lightgrey)

Практический проект по UI-автоматизации на **Python** с использованием **Playwright**, **Pytest** и архитектуры **Page Object Model (POM)**.

Проект создан для демонстрации навыков разработки и организации **automation framework для UI-тестирования веб-приложений**.

Основной акцент сделан не на полном покрытии сайта тестами, а на:

- построении структуры тестового проекта
- реализации архитектуры **Page Object Model**
- работе с локаторами и методами **Playwright**
- использовании **fixtures Pytest**
- организации тестов и повторно используемых компонентов
- генерации тестовых отчетов

---

# Technology Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Allure Report

---

# Implemented Test Scenarios

В проекте реализованы тестовые сценарии для отработки различных типов взаимодействия с веб-интерфейсом:

- авторизация пользователя
- проверка элементов интерфейса после логина
- работа с **checkbox / radio / switch**
- работа с **select и multi-select**
- взаимодействие с **таблицами**
- работа с **диалоговыми окнами**
- **drag and drop**
- **upload / download файлов**
- работа с **todo-элементами**
- создание **скриншотов элементов**

Проект используется для демонстрации различных методов Playwright:

- поиск элементов
- взаимодействие с UI
- ожидания элементов
- assertions
- работа со страницами через **Page Object Model**
---



# Example Test

Пример теста авторизации с использованием Page Object Model.

```python
def test_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("admin", "password123")

    assert login_page.is_logged_in()

```
Project Structure
```
Playwright/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── checkbox_page.py
│   ├── select_page.py
│   ├── dialog_page.py
│   ├── drag_and_drop_page.py
│   ├── table_page.py
│   ├── todo_page.py
│   └── upload_download_page.py
│
├── tests/
│   ├── auth/
│   │   └── test_login.py
│   └── forms/
│       ├── test_checkbox.py
│       ├── test_select_option.py
│       ├── test_dialogs.py
│       ├── test_drag_and_drop.py
│       ├── test_table.py
│       ├── test_upload_download.py
│       └── test_todo.py
│
├── data/
│   └── hello.txt
│
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```
---
Test Execution

Установка зависимостей:
```
pip install -r requirements.txt
```

Запуск тестов:
```
pytest
```

Запуск тестов с генерацией отчета Allure:
```
pytest --alluredir=allure-results
allure serve allure-results
```
---

## CI Pipeline

В проекте настроен **GitHub Actions CI pipeline**.

При каждом **push** и **pull request** автоматически выполняется:

- установка Python  
- установка зависимостей  
- установка браузеров Playwright  
- запуск тестов через `pytest`

---
