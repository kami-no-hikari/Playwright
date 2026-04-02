"""Простой мониторинг"""
# def test_listen_network(page: Page):
#     page.on("request", lambda request: print(">>", request.method, request.url))
#     page.on("response", lambda response: print("<<", response.status, response.url))
#     page.goto('https://osinit.ru/')

from playwright.sync_api import Page


def test_listen_only_api_requests(page: Page):
    requests_log = []
    responses_log = []

    def handle_request(request):
        if request.resource_type in ("xhr", "fetch") and "yandex" not in request.url:
            clean_url = request.url.split("?")[0]
            requests_log.append((request.method, clean_url))

    def handle_response(response):
        if response.request.resource_type in ("xhr", "fetch") and "yandex" not in response.url:
            clean_url = response.url.split("?")[0]
            responses_log.append((response.status, clean_url))

    page.on("request", handle_request)
    page.on("response", handle_response)

    page.goto("https://osinit.ru/")

    assert len(requests_log) > 0
    assert len(responses_log) > 0

    # print("\n=== REQUESTS ===")
    # print(f"{'METHOD':<8} | URL")
    # print("-" * 80)
    # for method, url in requests_log:
    #     print(f"{method:<8} | {url}")
    #
    # print("\n=== RESPONSES ===")
    # print(f"{'STATUS':<8} | URL")
    # print("-" * 80)
    # for status, url in responses_log:
    #     print(f"{status:<8} | {url}")
    #
    # print("\n=== RESPONSES ===")
    # print(f"{'STATUS':<8} | URL")
    # print("-" * 100)
    # for status, url in responses_log:
    #     print(f"{status:<8} | {url}")

