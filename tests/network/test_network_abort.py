from playwright.sync_api import Page


def test_abort_yandex_requests(page: Page):
    blocked_urls = []

    def handle_route(route):
        url = route.request.url

        if "yandex" in url:
            blocked_urls.append(url.split("?")[0])
            route.abort()
        else:
            route.continue_()

    page.route("**/*", handle_route)
    page.goto("https://osinit.ru/")

    assert len(blocked_urls) > 0

    # print("\n=== BLOCKED REQUESTS ===")
    # print(f"{'TYPE':<8} | URL")
    # print("-" * 80)
    # for url in blocked_urls:
    #     print(f"{'ABORT':<8} | {url}")