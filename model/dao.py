from core.models import BaseDAO
from typing import List


class AuthorDAO(BaseDAO):
    name: str = None
    twitter_handle: str = None


class MoneyControlNewsDAO(BaseDAO):
    header: str = None
    sub_header: str = None
    context: str = None
    source: str = None
    date_time: str = None
    html: str = None
    href: str = None
    author: AuthorDAO = None

    class Meta:
        table_name = "xbcbcbc_asas"





m = MoneyControlNewsDAO()
m.source ='money_control'
m.html = '<html> new html page </html>'
m.save()


