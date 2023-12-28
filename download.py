import zipfile
from pathlib import Path

import httpx
from bs4 import BeautifulSoup, Tag


def get_dpkg_url(data_url: str) -> str:
    resp_data = httpx.get(data_url, follow_redirects=True)
    resp_data.raise_for_status()
    resp_soup = BeautifulSoup(resp_data.content, "xml")
    root = resp_soup.find("test")
    assert root
    content = root.find("content")
    assert isinstance(content, Tag)
    dpkg_url = content.find("dataPackage")
    assert dpkg_url
    return dpkg_url.text


def download_extrace_dpkg(dpkg_url: str):
    resp = httpx.get(dpkg_url, follow_redirects=True)
    resp.raise_for_status()
    Path("data.zip").write_bytes(resp.content)
    Path("data").mkdir(exist_ok=True)
    zipfile.ZipFile("./data.zip").extractall("data")
    Path("data.zip").unlink()
