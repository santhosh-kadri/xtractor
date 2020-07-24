from abc import ABC

from bs4 import BeautifulSoup


class HtmlParser(BeautifulSoup, ABC):
    pass
