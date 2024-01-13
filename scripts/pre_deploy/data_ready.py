from zipfile import ZipFile

import httpx
from bs4 import BeautifulSoup, Tag
from pydantic import AnyHttpUrl

from ..base.config import SMSKB_DATA_URl
from ..base.const import TMP_FILE, TMP_PATH


def get_data_url(xml_file: AnyHttpUrl) -> str:
    response = httpx.get(xml_file)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "xml")
    root = soup.find("test")
    assert root
    content = root.find("content")
    assert isinstance(content, Tag)
    datapkg = content.find("dataPackage")
    assert datapkg
    print("Data zip url:", datapkg.text)
    return datapkg.text


def ready():
    data_url = get_data_url(SMSKB_DATA_URl)
    response = httpx.get(data_url)
    response.raise_for_status()
    TMP_FILE.write_bytes(response.content)
    tmp_file_zip = ZipFile(TMP_FILE)
    tmp_file_zip.extractall(TMP_PATH)
    del tmp_file_zip
    TMP_FILE.unlink()
