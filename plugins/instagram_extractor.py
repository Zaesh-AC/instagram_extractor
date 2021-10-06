import logging

from bs4 import BeautifulSoup
from plugins.settings import *


logger = logging.getLogger(__name__)


def extract_information(file):
    soup = BeautifulSoup(file, "html.parser")
    post = []
    divs = soup.find_all("div", {"class" : POST_CSS_CLASS})
    for div in divs:
        image = div.find("img")["src"]
        try:
            caption = div.find("div", {"class": CAPTION_CSS_CLASS}).text
        except Exception:
            caption = ""
        post.append((image, caption))
    return post