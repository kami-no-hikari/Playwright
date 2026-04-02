from playwright.sync_api import Page


def test_intercept_request(page: Page):
    was_called = False

    def handle(route):
        nonlocal was_called
        if "/api/users" in route.request.url:
            was_called = True
        route.continue_()

    page.route("**/*", handle)

    page.goto("https://reqres.in/")

    with page.expect_response("**/api/users?page=2"):
        page.evaluate("fetch('https://reqres.in/api/users?page=2')")

    assert was_called