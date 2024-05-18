import allure
import pytest
from faker import Faker

from base.base_test import BaseTest
from config.links import Links

fake = Faker()


@allure.feature('Авторизация пользователя')
class TestAuthUser(BaseTest):
    @allure.title('Авторизация пользователя с валидными данными')
    @allure.description('При проверке используются вальдные данные пользователя Aleska')
    @allure.severity('Critical')
    @pytest.mark.smoke
    def test_auth_valid_user(self):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()

        with allure.step('В поле логина вводим валидный логин'):
            self.login_page.field_username_input(self.User.LOGIN)

        with allure.step('В поле пароля вводим валидный пароль'):
            self.login_page.field_password_input(self.User.PASSWORD)

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.button_signin_click()

        with allure.step('Проверяем, что открыта страница рубрики'):
            self.rubric_page.is_opened()

    @allure.title('Авторизация пользователя с вальдным логином и пустым паролем')
    @allure.description('При проверке используются вальдный логин пользователя Aleska')
    @allure.severity('Trivial')
    def test_auth_valid_username_and_no_password(self):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()

        with allure.step('В поле логина вводим валидный логин'):
            self.login_page.field_username_input(self.User.login)

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.button_signin_click()

        with allure.step('Под полем пароль отображается текст валидации "Введи пароль"'):
            self.login_page.field_password_validation_message('Введи пароль')

    @allure.title('Авторизация пользователя с валидным логинов и паролем короче 6 символов')
    @allure.description('При проверке используются валидный логин пользователя Aleska')
    @allure.severity('Trivial')
    def test_auth_valid_username_and_a_password_shorter_than_6_characters(self):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()

        with allure.step('В поле логина вводим валидный логин'):
            self.login_page.field_username_input(self.User.login)

        with allure.step('В поле пароль вводим меньше 6 случайных символов'):
            self.login_page.field_password_input(fake.password(length=5))

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.button_signin_click()

        with allure.step(
                'Под полем пароль отображается текст валидации "Длина пароля должна быть не меньше 6 символов"'):
            self.login_page.field_username_validation_message('Длина пароля должна быть не меньше 6 символов')

    @allure.title('Авторизация пользователя без логина и пароля')
    @allure.description('При проверке используются не вводятся данные')
    @allure.severity('Critical')
    @pytest.mark.smoke
    def test_auth_no_username_and_no_password(self):
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

    @allure.title('Авторизация пользователя с валидным логин и паролем через API')
    @allure.description('При проверке используются валидный логин и пароль пользователя Aleska')
    @allure.severity('Critical')
    @pytest.mark.smoke
    def test_api_auth_valid_username_and_valid_password(self):
        with allure.step('Открыть страницу логина'):
            self.api_authorization.user(self.User.login, self.User.password)

        with allure.step('Проверяем, что открывается страница рубрик'):
            self.rubric_page.is_opened(Links.RUBRIC_PAGE)
