import os

def test_applitools_screenshots(applitools_page):
    applitools_page.make_page_screenshot()
    applitools_page.make_full_page_screenshot()
    applitools_page.make_form_screenshot()

    assert os.path.exists("screenshots/page.png")
    assert os.path.exists("screenshots/full_page.png")
    assert os.path.exists("screenshots/form.png")

    assert os.path.getsize("screenshots/page.png") > 0
    assert os.path.getsize("screenshots/full_page.png") > 0
    assert os.path.getsize("screenshots/form.png") > 0