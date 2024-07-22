import allure
import pytest
from faker import Faker

from base.base_test import BaseTest

fake = Faker()


@allure.feature('Профиль пользователя')
class TestProfile(BaseTest):
    @allure.title('Проверка открытия профиля пользователя')
    @allure.description('Проверяется, что при нажатии кнопки открывается профиль и видно Никнейм пользователя')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_open_user_profile(self, elements):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('В поле логина вводим валидный никнейм'):
            self.login_page.field_send_keys(element['Поле логин'], self.User.LOGIN)

        with allure.step('В поле пароля вводим валидный пароль'):
            self.login_page.field_send_keys(element['Поле пароль'], self.User.PASSWORD)

        with allure.step('Нажать кнопку "Войти"'):
            self.login_page.do_click(element['Кнопка войти'])

        with allure.step('Нажать кнопку'):
            element = elements['Панель навигации']
            self.app.do_click(element['Кнопка профиль'])
            element = elements['Профиль пользователя']
            self.assertion.text_in_element(element['Никнейм пользователя'], expected_text='Aleska')
