from playwright.sync_api import Page, Route


def test_mock_response_with_fetch_and_fulfill(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        json_data = response.json()
        json_data["title"] = "mocked title"
        route.fulfill(json=json_data)

    page.route("**/posts/1", handle_route)

    with page.expect_response("**/posts/1") as response_info:
        page.goto("https://example.com/")
        page.evaluate(
            """() => fetch('https://jsonplaceholder.typicode.com/posts/1')"""
        )

    response = response_info.value
    data = response.json()

    assert response.status == 200
    assert data["title"] == "mocked title"