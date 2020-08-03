import random
import requests
from typing import Union, Text
from requests.models import Response
from typing import List


class HttpProxy:
    """Class reads the proxies from a given file."""
    def __init__(self):
        self.proxy_list: List[dict] = self.__get_http_proxy()

    def __get_http_proxy(self) -> List[dict]:
        proxy_list: List[dict] = []
        with open('../http_proxies.txt')as proxy_file:
            for line in proxy_file:
                split_line = line.strip().split(':')
                proxy_ip = split_line[0]
                port = split_line[1]
                proxy_user = split_line[2]
                proxy_pass = split_line[3]
                proxy_list.append(
                    {f'https': f'https://{proxy_user}:{proxy_pass}@{proxy_ip}:{port}',
                     f'http': f'http://{proxy_user}:{proxy_pass}@{proxy_ip}:{port}',
                     })
        return proxy_list


class HttpRequest:
    """Class that is used to make http/https request and return the response
        Note: Fix need for -> currently we are using request library,
              but user should able to use any library of his choice
    """
    def __init__(self):
        self.__http_proxy_list: List[dict] = HttpProxy().proxy_list
        self.request = requests.Session()

    def get(self, url: Union[Text, bytes], **kwargs) -> Response:
        proxy_index = random.randint(0, len(self.__http_proxy_list) - 1)
        proxies = self.__http_proxy_list[proxy_index]
        return self.request.get(url, proxies=proxies)


