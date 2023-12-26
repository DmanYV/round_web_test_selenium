import allure
import faker

from data.base_test import BaseTest
from settings import Aleska

faker = faker.Faker()


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

    def test_auth_invalid_user(self):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()

        with allure.step('В поле логина вводим невалидный логин'):
            self.login_page.input_username_field(faker.user_name())

        with allure.step('В поле пароля вводим невалидный пароль'):
            self.login_page.input_password_field(faker.password())

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.click_signin_button()

        with allure.step('Проверить, что отображается попап с ошибкой авторизации'):
            self.login_page.check_popup_auth_error_visible('Ошибка авторизации')
            self.login_page.check_popup_auth_error_visible('Email/никнейм/номер телефона не зарегистрирован')

