import allure

from data.base_test import BaseTest
from settings import Administrator


class TestAuthUser(BaseTest):
    def test_auth_valid_user(self):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()

        with allure.step('В поле логина вводим валидный логин'):
            self.login_page.field_username_input(Administrator.login)

        with allure.step('В поле пароля вводим валидный пароль'):
            self.login_page.field_password_input(Administrator.password)

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.button_signin_click()
