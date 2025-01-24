import allure
import pytest
from faker import Faker

from base.base_test import BaseTest
from config.links import Links

fake = Faker()


@allure.feature('Меню профиля')
@pytest.mark.menu_profile
class TestMenuProfile(BaseTest):
    @allure.title('Проверка при нажатии в поп ап Редактировать профиль открывается страница редактирования')
    @allure.description('Проверяется на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_button_edit_user_profile(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку бургер-меню'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Проверить, что открылась страница редактирования профиля'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Редактировать профиль'])
            self.profile_page.element_is_not_visible(element['Редактировать профиль'])

        with allure.step('Проверить, что заголовок страницы "Редактировать профиль"'):
            element = elements['Общие']
            self.assertion.text_in_element(element['Заголовок страницы'], expected_text='Редактировать профиль')

    @allure.title('Проверка при нажатии в поп ап Пригласить друга открывается страница приглашения')
    @allure.description('Проверяется на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_pop_up_menu_click_button_invite_friend(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку бургер-меню'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Проверить, что открылась страница редактирования профиля'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Пригласить друга'])

        with allure.step('Проверить, что заголовок страницы "Редактировать профиль"'):
            element = elements['Страница пригласить друга']
            self.assertion.text_in_element(element['Заголовок страницы'], expected_text='Пригласить друга')

    @allure.title('Проверка при нажатии в поп ап Лайки открывается страница лайков пользователя')
    @allure.description('Проверяется на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_pop_up_menu_click_button_likes(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку бургер-меню'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать на кнопку Лайки'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Лайки'])
            self.profile_page.element_is_not_visible(element['Лайки'])
        with allure.step('Проверить, что заголовок страницы "Лайки"'):
            element = elements['Общие']
            self.assertion.text_in_element(element['Заголовок страницы'], expected_text='Лайки')

    @allure.title('Проверка при нажатии в поп ап Избранное открывается страница избранного пользователя')
    @allure.description('Проверяется на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_pop_up_menu_click_button_favorite(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку бургер-меню'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать на кнопку Избранное'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Избранное'])
            self.profile_page.element_is_not_visible(element['Избранное'])

        with allure.step('Проверить, что заголовок страницы "Избранное"'):
            element = elements['Общие']
            self.assertion.text_in_element(element['Заголовок страницы'], expected_text='Избранное')

    @allure.title('Проверка при нажатии в поп ап Тех. поддержка открывается окно кэррота')
    @allure.description('Проверяется на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    @pytest.mark.skip(reason="Не работает в безголовом режиме")
    def test_pop_up_menu_click_button_technical_support(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку бургер-меню'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать на кнопку Тех. поддержка'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Тех. поддержка'])

        with allure.step('Проверить, что открылось окно кэррота'):
            element = elements['Кэррот']
            self.assertion.is_elem_displayed(element['Чат кэррот'])

    @allure.title('Проверка при нажатии в поп ап О системе открывается страница О системе')
    @allure.description('Проверяется на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_pop_up_menu_click_button_about_system(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку бургер-меню'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать на кнопку О системе'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['О системе'])
            self.profile_page.element_is_not_visible(element['О системе'])

        with allure.step('Проверить, что заголовок страницы "О системе"'):
            element = elements['Общие']
            self.assertion.text_in_element(element['Заголовок страницы'], expected_text='О системе')

    @allure.title('Проверка при нажатии в поп ап Выйти их аккаунта открывается страница авторизации')
    @allure.description('Проверяется на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_pop_up_menu_click_button_logout(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку бургер-меню'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать на кнопку Выйти их аккаунта'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Выйти из аккаунта'])

        with allure.step('Проверить, что открылась страница авторизации'):
            self.assertion.page_is_opened(Links.AUTHORIZATION_PAGE)
