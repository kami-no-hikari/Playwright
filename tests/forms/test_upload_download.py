import os

def test_file_upload(upload_download_page):
    upload_download_page.navigate()

    file_path = os.path.abspath("data/hello.txt")
    upload_download_page.upload_file(file_path)

    uploaded_text = upload_download_page.get_uploaded_file_text()

    assert "hello.txt" in uploaded_text


def test_file_download(upload_download_page):
    upload_download_page.navigate()

    download_dir = os.path.abspath("data/downloads")
    os.makedirs(download_dir, exist_ok=True)

    saved_file_path = upload_download_page.download_file(download_dir)

    assert os.path.exists(saved_file_path)
    assert os.path.getsize(saved_file_path) > 0