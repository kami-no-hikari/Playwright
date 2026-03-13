import os
from pages.base_page import BasePage


class UploadDownloadPage(BasePage):
    URL = "https://demoqa.com/upload-download"

    def __init__(self, page):
        super().__init__(page)
        self.upload_input = page.locator("#uploadFile")
        self.submit_upload_text = page.locator("#uploadedFilePath")
        self.download_button = page.locator("#downloadButton")

    def navigate(self):
        self.open(self.URL)

    def upload_file(self, file_path: str):
        self.upload_input.set_input_files(file_path)

    def get_uploaded_file_text(self):
        return self.submit_upload_text.inner_text()

    def download_file(self, download_dir: str):
        with self.page.expect_download() as download_info:
            self.download_button.click()

        download = download_info.value
        file_name = download.suggested_filename
        full_path = os.path.join(download_dir, file_name)
        download.save_as(full_path)

        return full_path