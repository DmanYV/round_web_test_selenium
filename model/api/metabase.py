import time

import requests
from requests.cookies import RequestsCookieJar

from config.links import MetaBaseLinks
from base.base_page import BasePage


class MetaBase(BasePage):
    PAGE_URL = MetaBaseLinks.HOST

    def authorization(self, username: str, password: str) -> RequestsCookieJar:
        """
        Метод получения Session_ID в Metabase через API.

        :param username: Логин пользователя
        :param password: Пароль пользователя
        :return: cookies: Возвращает куки
        """
        json = {
            'username': username,
            'password': password,
            'remember': True
        }

        response = requests.post(url=MetaBaseLinks.AUTHORIZATION, json=json)
        cookies = response.cookies
        return cookies

    def take_last_code(self, cookies: RequestsCookieJar) -> str:
        """
        Метод получения Session_ID в Metabase через API.

        :param cookies: Куки авторизации
        :return: last_code: Последний созданный код в таблице
        """
        cookies = cookies
        json = {"type": "query",
                "query": {"source-table": 121,
                          "filter": ["time-interval",
                                     ["field", 726, None],
                                     "current",
                                     "day",
                                     {"include_current": True}],
                          "order-by": [["desc", ["field", 728, None]]]},
                "database": 5,
                "parameters": []}
        time.sleep(1)
        response = requests.post(url=MetaBaseLinks.DATA_SATE, cookies=cookies, json=json)
        last_code = response.json()['data']['rows'][0][7]
        return last_code