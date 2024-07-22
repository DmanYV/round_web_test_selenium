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
    def test_open_user_profile(self, elements, login_to_app):
        with allure.step('Нажать на кнопку профиль'):
            element = elements['Панель навигации']
            self.app.do_click(element['Кнопка профиль'])

        with allure.step('Проверить, что отображается никнейм Aleska'):
            element = elements['Профиль пользователя']
            self.assertion.text_in_element(element['Никнейм пользователя'], expected_text='Aleska')
