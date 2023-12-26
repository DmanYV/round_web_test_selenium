import allure

from data.base_test import BaseTest
from settings import Aleska


class TestAuthUser(BaseTest):
    def test_auth_valid_user(self):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()

        with allure.step('В поле логина вводим валидный логин'):
            self.login_page.input_username_field(Aleska.login)

        with allure.step('В поле пароля вводим валидный пароль'):
            self.login_page.input_password_field(Aleska.password)

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.click_signin_button()
