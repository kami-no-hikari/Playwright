# Playwright UI Automation Framework

![CI](https://github.com/kami-no-hikari/Playwright/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.14-blue)
![Playwright](https://img.shields.io/badge/playwright-automation-green)
![Pytest](https://img.shields.io/badge/pytest-framework-orange)

Практический проект по автоматизации тестирования на **Python** с использованием **Playwright**, **Pytest** и архитектуры **Page Object Model (POM)**.
Проект демонстрирует навыки разработки **UI и API автотестов**, организацию **CI pipeline**, а также генерацию и публикацию **Allure отчётов**.

---

## Technology Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Requests (API тестирование)
- Allure Report
- GitHub Actions CI
- GitHub Pages (публикация отчётов)

---

## Project Structure

```
Playwright
│
├── pages                # Page Object модели
│
├── tests
│   ├── api              # API тесты
│   │   └── test_posts_api.py
│   │
│   ├── auth             # тесты авторизации
│   └── forms            # UI тесты
│
├── .github/workflows
│   └── tests.yml        # CI pipeline
│
├── data
├── conftest.py
├── requirements.txt
└── README.md
```

---

## Implemented Test Types

### UI Testing

- тестирование веб-интерфейса через Playwright
- архитектура **Page Object Model**
- работа с различными UI элементами
- загрузка и скачивание файлов
- drag and drop
- таблицы
- формы
- скриншоты при падении тестов

### API Testing

- тестирование REST API через `requests`
- проверка HTTP статусов
- проверка JSON ответов

---

## CI Pipeline

В проекте настроен **GitHub Actions CI pipeline**.

При каждом **push** и **pull request** автоматически выполняется:

1. установка Python
2. установка зависимостей проекта
3. установка браузеров Playwright
4. запуск тестов через pytest
5. генерация Allure отчёта
6. публикация отчёта на GitHub Pages

---

## Allure Report

После каждого запуска CI автоматически публикуется **HTML отчёт Allure**.

Открыть отчёт:

https://kami-no-hikari.github.io/Playwright/

---

## Running Tests Locally

Установка зависимостей:

```
pip install -r requirements.txt
```

Установка браузеров Playwright:

```
playwright install
```

Запуск тестов:

```
pytest -n 2 -v --alluredir=allure-results
```

Просмотр Allure отчёта:

```
allure serve allure-results
```

---

## Key Features

- UI automation framework на Python
- использование **Playwright API**
- архитектура **Page Object Model**
- API тестирование через **requests**
- параллельный запуск тестов
- CI pipeline через **GitHub Actions**
- публикация **Allure отчётов**
