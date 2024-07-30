import time

import allure
import pytest
from faker import Faker

from base.base_test import BaseTest
from settings import User

fake = Faker()


@allure.feature('Редактирование профиля')
class TestEditingProfile(BaseTest):
    @allure.title('Проверка можно изменить никнейм')
    @allure.description('Проверяется на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_you_can_change_your_nickname(self, elements, login_to_app):
        with allure.step('Нажать кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Запомнить никнейм пользователя'):
            element = elements['Общие']
            self.profile_page.get_element_text(element['Заголовок страницы'])

        with allure.step('Нажать на кнопку редактирования никнейма'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать "Редактировать профиль"'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Редактировать профиль'])

        with allure.step('Очистить поле Никнейм'):
            element = elements['Страница редактировать профиль']
            self.edit_profile_page.clear(element['Поле никнейм'])

        with (allure.step('Ввести в поле рандомный никнейм')):
            new_username = fake.user_name()
            self.edit_profile_page.field_send_keys(element['Поле никнейм'], text=new_username)

        with allure.step('Нажать кнопку Сохранить'):
            self.edit_profile_page.scroll_to_elem(element['Кнопка сохранить'])
            self.edit_profile_page.do_click(element['Кнопка сохранить'])

        with allure.step('Проверить, что отображается новый никнейм пользователя'):
            element = elements['Общие']
            self.assertion.text_in_element(element['Заголовок страницы'], expected_text=new_username)

        with allure.step('Вернуть профилю никнейм Aleska'):
            self.edit_profile_page.change_username(username='Aleska')

    @allure.title('Проверка невозможно поменять никнейм на дубликат который есть уже в система')
    @allure.description('Проверяется на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_it_is_impossible_to_save_an_already_taken_nickname(self, elements, login_to_app):
        with allure.step('Изменить никнейм пользователя на уже зарегистрированный Natalya'):
            self.edit_profile_page.change_username(username='Natalya')

        with allure.step('Проверить, что появилось уведомление'):
            element = elements['Страница редактировать профиль']
            self.assertion.is_elem_displayed(element['Поп ап уведомление'])

        with allure.step('Нажать на кнопку Профиль'):
            self.app.profile_button_click()

        with allure.step('Проверить, что в заголовке остался старый никнейм'):
            element = elements['Общие']
            self.assertion.text_in_element(element['Заголовок страницы'], expected_text=User.LOGIN)
