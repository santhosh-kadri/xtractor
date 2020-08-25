import settings

from dataclasses import dataclass
from argparse import ArgumentParser
from core.http_service import HttpRequest
from core.parser_service import HtmlParser
from core.db_service import AlchemyService
from core.logger import Logger
from requests.exceptions import ProxyError


@dataclass
class BaseExtractor:
    """ All xtractor needs to be extended to this base class."""
    request = HttpRequest()
    arg_parser = ArgumentParser('scraper')
    cmd_args = None
    db = AlchemyService()
    log = None

    def execute(self):
        raise XtendedExcpetion('Method execute not implemented')

    def parse_html(self, html, parser='html.parser'):
        return HtmlParser(html, parser)

    def add_cmd_argument(self, arg_parser):
        return self.arg_parser

    def __init_arg_parser(self):
        self.arg_parser = self.init_xtarctor()

    def run(self):
        self.log = Logger(self.__class__.__name__)
        try:
            self.add_cmd_argument(self.arg_parser)
            self.cmd_args = self.arg_parser.parse_args()
            self.execute()
        except Exception as e:
            self.log.error(str(e))
