import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.checkbox_page import CheckboxPage
from pages.select_page import SelectPage
from pages.upload_download_page import UploadDownloadPage
from pages.todo_page import TodoPage
from pages.drag_and_drop_page import DragAndDrop
from pages.dialog_page import DialogPage
from pages.table_page import TablePage
from pages.applitools_page import ApplitoolsPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)


@pytest.fixture
def checkbox_page(page):
    return CheckboxPage(page)


@pytest.fixture
def select_page(page):
    return SelectPage(page)


@pytest.fixture
def download_page(page):
    return DownloadPage(page)


# @pytest.fixture
# def todo_page(page):
#     return TodoPage(page)


@pytest.fixture
def upload_page(page):
    return UploadPage(page)


@pytest.fixture
def upload_download_page(page):
    return UploadDownloadPage(page)


@pytest.fixture
def todo_page(page):
    return TodoPage(page)

@pytest.fixture
def drag_and_drop_page(page):
    return DragAndDrop(page)

@pytest.fixture
def dialog_page(page):
    return DialogPage(page)


@pytest.fixture
def table_page(page):
    table_page = TablePage(page)
    table_page.open_page()
    return table_page

@pytest.fixture
def applitools_page(page):
    applitools_page = ApplitoolsPage(page)
    applitools_page.open_page()
    return applitools_page