import allure
import pytest
from faker import Faker

from base.base_test import BaseTest
from settings import User

fake = Faker()
fakeru = Faker("ru_RU")


@allure.feature('Редактирование профиля')
@pytest.mark.editing_profile
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
            self.edit_profile_page.scroll_to_element(element['Кнопка сохранить'])
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

    @allure.title('Проверка максимальное количество символов для ввода в поле о себе 140')
    @allure.description('Проверяется на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_max_length_of_description(self, elements, login_to_app):
        with allure.step('Нажать кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку редактирования профиля'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать "Редактировать профиль"'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Редактировать профиль'])

        with allure.step('Ввести в поле о себе текст более 140 символов'):
            element = elements['Страница редактировать профиль']
            self.edit_profile_page.field_send_keys(element['Поле о себе'], fake.pystr(min_chars=141, max_chars=250))

        with allure.step('Проверить, что в поле ввелось 140 символов'):
            self.assertion.length_simbols_in_text(element['Поле о себе'], length=140)

    @allure.title('Проверка возможности ввода и сохранения описания на кириллице')
    @allure.description('Проверяется на пользователе Aleska, после теста о себе очищается и сохраняется')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_the_ability_to_enter_and_save_descriptions_in_cyrillic(self, elements, login_to_app):
        with allure.step('Нажать кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку редактирования профиля'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать "Редактировать профиль"'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Редактировать профиль'])

        with allure.step('Ввести в поле о себе текст на кириллице'):
            element = elements['Страница редактировать профиль']
            about_text = fakeru.text(max_nb_chars=140)
            self.edit_profile_page.field_send_keys(element['Поле о себе'], text=about_text)

        with allure.step('Нажать кнопку Сохранить'):
            self.edit_profile_page.scroll_to_element(element['Кнопка сохранить'])
            self.edit_profile_page.do_click(element['Кнопка сохранить'])

        with allure.step('Проверить, что в профиле в поле о себе отображается тот же текст'):
            element = elements['Профиль пользователя']
            self.assertion.text_in_element(element['О себе'], expected_text=about_text)

        with allure.step('Очистить текст в О себе'):
            self.edit_profile_page.clear_about()
