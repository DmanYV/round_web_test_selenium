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
    @allure.description(
        'Проверяется, что при открытие профиля отображаются проекты ожидающих модерации в количестве > 0')
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
    @allure.description(
        'Проверяется, что при открытие профиля в нем отображаются проекты заблокированных проектов в количестве > 0')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_display_blocked_projects(self, elements, login_to_app):
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Проверить, что количество заблокированных проектов > 0 и проект видим'):
            element = elements['Профиль пользователя']
            self.assertion.length_elements(element['Проект заблокирован'], length=0)
            self.assertion.is_elem_displayed(element['Проект заблокирован'])

    @allure.title('Проверить обновление счетчика просмотров проекта')
    @allure.description('Проверить, что счетчик изменяется при входе и открытии страницы')
    @allure.severity('Critical')
    @pytest.mark.mionor
    def test_update_views_counter(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Запомнить сколько просмотров на счетчике у первого проекта пользователя'):
            element = elements['Профиль пользователя']
            initial_views = self.profile_page.find_elements(element['Счетчик просмотров проекта'])[3].text

        with allure.step('Перейти в проект'):
            self.profile_page.refresh()

        with allure.step('Запомнить количество просмотров, после обновления страницы'):
            current_views = self.profile_page.find_elements(element['Счетчик просмотров проекта'])[3].text
            self.assertion.values_is_equal(int(current_views), int(initial_views) + 1)

    @allure.title('Проверка возможности просмотреть свои ачивки в профиле')
    @allure.description('Проверка происходит на пользователе Aleska у которого есть ачивки')
    @allure.severity('Critical')
    @pytest.mark.mionor
    def test_the_ability_to_view_your_achievements_in_your_profile(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Проверить, что отображается блок ачивок'):
            element = elements['Профиль пользователя']
            self.assertion.is_elem_displayed(element['Блок ачивок'])

        with allure.step('Проверить, что отображается кнопка Все'):
            self.assertion.is_elem_displayed(element['Кнопка все'])

    @allure.title('Проверка возможности просмотреть детальный экран ачивки')
    @allure.description('Проверка происходит на пользователе Aleska у которого есть ачивки')
    @allure.severity('Critical')
    @pytest.mark.mionor
    def test_the_ability_to_view_the_detailed_achievement_screen(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать первую ачивку в списке'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Блок ачивок'])

        with allure.step('Проверить, что открылось модальное окно с описанием ачивки'):
            element = elements['Банк ачивок']
            self.assertion.is_elem_displayed(element['Модальное окно ачивки'])