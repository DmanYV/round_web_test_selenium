import requests

from config.links import Api, Links
from base.base_page import BasePage


class ApiAuthorization(BasePage):
    PAGE_URL = Links.MAIN_PAGE

    def user(self):
        headers = {
            'X-Client-Id': 'round',
            'X-Client-Type': 'web',
            'X-Language': 'ru'
        }
        data = {
            'client_id': 'Krujok.Online.Mobile',
            'grant_type': 'password',
            'username': 'Aleska',
            'password': 'qwe123'
        }

        response = requests.post(url=Api.TOKEN, headers=headers, data=data)
        access_token = response.json()["access_token"]
        assert response.status_code == 200
        assert response.json()["access_token"] is not None
        assert response.json()['token_type'] == 'Bearer'
        self.open()
        self.driver.execute_script("window.localStorage.setItem" "(arguments[0], arguments[1]);", 'access_token',
                                   access_token)
        self.open()
