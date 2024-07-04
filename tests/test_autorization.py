import allure
import pytest
from faker import Faker

from base.base_test import BaseTest

fake = Faker()


@allure.feature('Авторизация пользователя')
class TestAuthUser(BaseTest):
    @allure.title('Авторизация пользователя с валидными данными по логину')
    @allure.description('При проверке используются валидные данные пользователя Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_auth_valid_user(self, elements):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('В поле логина вводим валидный никнейм'):
            self.login_page.field_send_keys(element['Поле логин'], self.User.LOGIN)

        with allure.step('В поле пароля вводим валидный пароль'):
            self.login_page.field_send_keys(element['Поле пароль'], self.User.PASSWORD)

        with (allure.step('Нажать кнопку "Войти"')):
            self.login_page.do_click(element['Кнопка войти'])

        with allure.step('Проверяем, что открыта страница рубрики'):
            self.assertion.page_is_opened(self.rubric_page.PAGE_URL)

    @allure.title('Авторизация пользователя с валидными данными по номеру телефона')
    @allure.description('При проверке используются валидные данные пользователя Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_authorization_of_a_user_with_valid_data_by_phone_number(self, elements):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('В поле логина вводим валидный номер телефона'):
            self.login_page.field_send_keys(element['Поле логин'], self.User.PHONE)

        with allure.step('В поле пароля вводим валидный пароль'):
            self.login_page.field_send_keys(element['Поле пароль'], self.User.PASSWORD)

        with (allure.step('Нажать кнопку "Войти"')):
            self.login_page.do_click(element['Кнопка войти'])

        with allure.step('Проверяем, что открыта страницу рубрики'):
            self.assertion.page_is_opened(self.rubric_page.PAGE_URL)

    @allure.title('Авторизация пользователя с валидными данными по почтовому адресу')
    @allure.description('При проверке используются валидные данные пользователя Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_authorization_of_a_user_with_valid_data_by_email(self, elements):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('В поле логина вводим валидный почтовый адрес'):
            self.login_page.field_send_keys(element['Поле логин'], self.User.EMAIL)

        with allure.step('В поле пароля вводим валидный пароль'):
            self.login_page.field_send_keys(element['Поле пароль'], self.User.PASSWORD)

        with (allure.step('Нажать кнопку "Войти"')):
            self.login_page.do_click(element['Кнопка войти'])

        with allure.step('Проверяем, что открыта страницу рубрики'):
            self.assertion.page_is_opened(self.rubric_page.PAGE_URL)

    @allure.title('Авторизация пользователя с валидным логином и пустым паролем')
    @allure.description('При проверке используются валидный логин пользователя Aleska')
    @allure.severity('Trivial')
    @pytest.mark.regression
    def test_auth_valid_username_and_no_password(self, elements):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('В поле логина вводим валидный логин'):
            self.login_page.field_send_keys(element['Поле логин'], self.User.LOGIN)

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.do_click(element['Кнопка войти'])

        with allure.step('Под полем пароль отображается текст валидации "Введи пароль"'):
            self.assertion.text_in_element(element['Валидация поля пароль'], 'Введи пароль')

    @allure.title('Авторизация пользователя с валидным логинов и паролем короче 6 символов')
    @allure.description('При проверке используются валидный логин пользователя Aleska')
    @allure.severity('Trivial')
    @pytest.mark.regression
    def test_auth_valid_username_and_a_password_shorter_than_6_characters(self, elements):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('В поле логина вводим валидный логин'):
            self.login_page.field_send_keys(element['Поле логин'], self.User.LOGIN)

        with allure.step('В поле пароль вводим меньше 6 случайных символов'):
            self.login_page.field_send_keys(element['Поле пароль'], fake.password(length=5))

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.do_click(element['Кнопка войти'])

        with allure.step(
                'Да-да, мы не любим хакеров, поэтому присутствие цифр обязательно. '
                'И еще, принимаются пароли только на английском языке от 6 символов"'):
            self.assertion.text_in_element(element['Валидация поля пароль'],
                                           'Да-да, мы не любим хакеров, поэтому присутствие цифр обязательно. '
                                           'И еще, принимаются пароли только на английском языке от 6 символов')

    @allure.title('Авторизация пользователя без логина и пароля')
    @allure.description('При проверке не вводятся данные')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_auth_no_username_and_no_password(self, elements):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.do_click(element['Кнопка войти'])

        with allure.step('Под полем Никнейм или номер телефона отображается текст валидации '
                         '"Введи e-mail, никнейм или номер телефона, указанные при регистрации"'):
            self.assertion.text_in_element(element['Валидация поля логин'],
                                           'Введи Никнейм или номер телефона')

        with allure.step('Под полем пароль отображается текст валидации '
                         '"Введи пароль"'):
            self.assertion.text_in_element(element['Валидация поля пароль'],
                                           'Введи пароль')

    @allure.title('Авторизация пользователя с валидным логин и паролем через API')
    @allure.description('При проверке используются валидный логин и пароль пользователя Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_api_auth_valid_username_and_valid_password(self):
        with allure.step('Открыть страницу логина'):
            self.api_authorization.user(self.User.LOGIN, self.User.PASSWORD)

        with allure.step('Проверяем, что открывается страница рубрик'):
            self.assertion.page_is_opened(self.rubric_page.PAGE_URL)
