import requests
import allure


@allure.feature("API")
@allure.story("Get single post")
def test_get_single_post(api_session, api_base_url):
    with allure.step("Отправить GET запрос на получение поста с id=1"):
        response = api_session.get(f"{api_base_url}/posts/1")

    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == 200

    with allure.step("Преобразовать ответ в JSON"):
        data = response.json()

    with allure.step("Проверить структуру ответа"):
        assert data["id"] == 1
        assert "title" in data
        assert "body" in data


@allure.feature("API")
@allure.story("Get posts list")
def test_get_posts_list(api_session, api_base_url):
    with allure.step("Отправить GET запрос на получение списка постов"):
        response = api_session.get(f"{api_base_url}/posts")

    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == 200

    with allure.step("Преобразовать ответ в JSON"):
        data = response.json()

    with allure.step("Проверить, что вернулся список постов"):
        assert isinstance(data, list)
        assert len(data) > 0
        assert "id" in data[0]


@allure.feature("API")
@allure.story("Create post")
def test_create_post(api_session, api_base_url):
    payload = {
        "title": "test post",
        "body": "automation test",
        "userId": 1
    }

    with allure.step("Отправить POST запрос на создание поста"):
        response = api_session.post(f"{api_base_url}/posts", json=payload)

    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == 201

    with allure.step("Преобразовать ответ в JSON"):
        data = response.json()

    with allure.step("Проверить, что данные ответа совпадают с payload"):
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]


@allure.feature("API")
@allure.story("Get invalid post")
def test_get_invalid_post(api_session, api_base_url):
    with allure.step("Отправить GET запрос на несуществующий пост"):
        response = api_session.get(f"{api_base_url}/posts/999999")

    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == 404