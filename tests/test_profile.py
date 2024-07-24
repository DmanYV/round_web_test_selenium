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
            self.app.profile_button_click()

        with allure.step('Проверить, что отображается никнейм Aleska'):
            element = elements['Профиль пользователя']
            self.assertion.text_in_element(element['Никнейм пользователя'], expected_text='Aleska')

    @allure.title('Проверка возможности просмотреть все свои проекты в профиле')
    @allure.description('Проверяется, что при открытие профиля в нем отображаются проекты в количестве > 0')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_open_user_profile(self, elements, login_to_app):
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Проверить, что количество проектов > 0'):
            element = elements['Профиль пользователя']
            self.assertion.length_elements(element['Список проектов'])

    @allure.title('Проверить отображения проектов ожидающих модерации')
    @allure.description('Проверяется, что при открытие профиля отображаются проекты ожидающих модерации в количестве > 0')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_displays_projects_awaiting_moderation(self, elements, login_to_app):
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Проверить, что количество проектов ожидающих модерации > 0 и проект видим'):
            element = elements['Профиль пользователя']
            self.assertion.length_elements(element['Проект ожидает модерации'], length=0)
            self.assertion.is_elem_displayed(element['Проект ожидает модерации'])

    @allure.title('Проверить отображение заблокированных проектов')
    @allure.description('Проверяется, что при открытие профиля в нем отображаются проекты заблокированных проектов в количестве > 0')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_display_blocked_projects(self, elements, login_to_app):
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Проверить, что количество заблокированных проектов > 0 и проект видим'):
            element = elements['Профиль пользователя']
            self.assertion.length_elements(element['Проект заблокирован'], length=0)
            self.assertion.is_elem_displayed(element['Проект заблокирован'])
