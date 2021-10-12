import logging

from bs4 import BeautifulSoup
from settings import POST_CSS_CLASS, CAPTION_CSS_CLASS


logger = logging.getLogger(__name__)


def extract_information(file):
    soup = BeautifulSoup(file, "html.parser")
    divs = soup.find_all("div", {"class" : POST_CSS_CLASS})
    return [
        (div.find("img")["src"], div.find("div", {"class": CAPTION_CSS_CLASS}).text)
        for div in divs
    ]