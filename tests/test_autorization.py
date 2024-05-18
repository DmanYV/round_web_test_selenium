import allure
from faker import Faker

from base.base_test import BaseTest
from settings import User
from config.links import Links

fake = Faker()


class TestAuthUser(BaseTest):
    def test_auth_valid_user(self):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()

        with allure.step('В поле логина вводим валидный логин'):
            self.login_page.field_username_input(User.login)

        with allure.step('В поле пароля вводим валидный пароль'):
            self.login_page.field_password_input(User.password)

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.button_signin_click()

        with allure.step('Проверяем, что открыта страница рубрики'):
            self.rubric_page.is_opened()

    def test_auth_valid_username_and_no_password(self):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()

        with allure.step('В поле логина вводим валидный логин'):
            self.login_page.field_username_input(User.login)

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.button_signin_click()

        with allure.step('Под полем пароль отображается текст валидации "Введи пароль"'):
            self.login_page.field_password_validation_message('Введи пароль')

    def test_auth_valid_username_and_a_password_shorter_than_6_characters(self):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()

        with allure.step('В поле логина вводим валидный логин'):
            self.login_page.field_username_input(User.login)

        with allure.step('В поле пароль вводим меньше 6 случайных символов'):
            self.login_page.field_password_input(fake.password(length=5))

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.button_signin_click()

        with allure.step('Под полем пароль отображается текст валидации "Длина пароля должна быть не меньше 6 символов"'):
            self.login_page.field_username_validation_message('Длина пароля должна быть не меньше 6 символов')

    def test_auth_no_login(self):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.button_signin_click()

        with allure.step('Под полем Никнейм, email или номер телефона отображается текст валидации '
                         '"Введи e-mail, никнейм или номер телефона, указанные при регистрации"'):
            self.login_page.field_username_validation_message('Введи e-mail, никнейм или номер телефона, '
                                                              'указанные при регистрации')

        with allure.step('Под полем пароль отображается текст валидации '
                         '"Введи пароль"'):
            self.login_page.field_password_validation_message('Введи пароль')

    def test_api_auth(self):
        with allure.step('Открыть страницу логина'):
            self.api_authorization.user()

        with allure.step('Проверяем, что открывается страница рубрик'):
            self.rubric_page.is_opened(Links.RUBRIC_PAGE)
