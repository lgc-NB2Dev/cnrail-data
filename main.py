from .config import SMSKB_XML_URL
from .download import download_extrace_dpkg, get_dpkg_url


def main():
    download_extrace_dpkg(get_dpkg_url(SMSKB_XML_URL))
