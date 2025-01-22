import time

import allure
import pytest
from faker import Faker

from base.base_test import BaseTest
from settings import User
from fixtures.fixtures_for_registration_tests import registration_user

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
            element_profile = elements['Профиль пользователя']
            self.profile_page.do_click(element_profile['Кнопка бургер-меню'])

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
            self.profile_page.find_element(element_profile['О себе'])
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

    @pytest.mark.parametrize('options', [
        'У меня есть другой профиль в ROUND!',
        'Мои проекты не комментируют и не лайкают',
        'Ведение аккаунта отнимает у меня много времени',
        'Не нашел (-ла) интересного для себя контента',
        'Удаляю по просьбе родителей',
        'Меня беспокоит безопасность моих данных'
    ])
    @allure.title('Проверка удаления аккаунта по причине "{options}"')
    @allure.description(
        'Сначала регистрируется новый пользователь, '
        'после удаляется по причине и проверяется, что при авторизации ему отображается уведомление')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_deletion_of_account(self, elements, registration_user, options):
        with allure.step('Нажать кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Закрыть анкету'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка закрыть анкету'])

        with allure.step('Запомнить никнейм пользователя'):
            element = elements['Общие']
            username = self.profile_page.get_element_text(element['Заголовок страницы'])

        with allure.step('Нажать на бургер-меню'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать на Редактировать профиль'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Редактировать профиль'])

        with allure.step('Нажать на Настройки аккаунта'):
            element = elements['Страница редактировать профиль']
            self.edit_profile_page.do_click(element['Настройки аккаунта'])

        with allure.step('Нажать удалить аккаунт'):
            element = elements['Страница настройки аккаунта']
            self.settings_page.do_click(element['Удалить аккаунт'])

        with allure.step('Нажать кнопку Удалить'):
            self.settings_page.do_click(element['Кнопка удалить'])

        with allure.step(f'Выбрать вариант "{options}"'):
            self.checkbox.checkbox_on(element[options])

        with allure.step('Нажать кнопку удалить аккаунт'):
            self.settings_page.do_click(element['Кнопка удалить аккаунт'])

        with allure.step('Нажать кнопку Хорошо'):
            # Задублирован метод для обхода падения
            self.settings_page.do_click(element['Кнопка хорошо'])
            self.settings_page.do_click(element['Кнопка хорошо'])

        with allure.step('Нажать Войти'):
            element = elements['Страница авторизации']
            self.authorization_page.do_click(element['Кнопка войти'])

        with allure.step('В поле никнейм ввести никнейм пользователя'):
            element = elements['Страница логина']
            self.authorization_page.field_send_keys(element['Поле логин'], text=username)

        with allure.step('В поле пароль ввести пароль'):
            self.authorization_page.field_send_keys(element['Поле пароль'], text=User.PASSWORD)

        with allure.step('Нажать кнопку Войти'):
            self.authorization_page.do_click(element['Кнопка войти'])

        with allure.step('Проверить, что появилось уведомление для пользователя'):
            self.assertion.is_elem_displayed(element['Уведомление аккаунт удален'])

    @allure.title('Проверка удаления аккаунта по причине "Другая причина"')
    @allure.description(
        'Сначала регистрируется новый пользователь, '
        'после удаляется по причине и проверяется, что при авторизации ему отображается уведомление')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_deletion_of_account_another_reason(self, elements, registration_user):
        with allure.step('Нажать кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Закрыть анкету'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка закрыть анкету'])

        with allure.step('Запомнить никнейм пользователя'):
            element = elements['Общие']
            username = self.profile_page.get_element_text(element['Заголовок страницы'])

        with allure.step('Нажать на бургер-меню'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать на Редактировать профиль'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Редактировать профиль'])

        with allure.step('Нажать на Настройки аккаунта'):
            element = elements['Страница редактировать профиль']
            self.edit_profile_page.do_click(element['Настройки аккаунта'])

        with allure.step('Нажать удалить аккаунт'):
            element = elements['Страница настройки аккаунта']
            self.settings_page.do_click(element['Удалить аккаунт'])

        with allure.step('Нажать кнопку Удалить'):
            self.settings_page.do_click(element['Кнопка удалить'])

        with allure.step(f'Выбрать вариант "Другая причина"'):
            self.checkbox.checkbox_on(element['Другая причина'])

        with allure.step('В поле причины ввести какой либо текст'):
            self.settings_page.field_send_keys(element['Поле причина удаления'], text=fakeru.text(max_nb_chars=120))

        with allure.step('Нажать кнопку удалить аккаунт'):
            self.settings_page.do_click(element['Кнопка удалить аккаунт'])

        with allure.step('Нажать кнопку Хорошо'):
            # Задублирован метод для обхода падения
            self.settings_page.do_click(element['Кнопка хорошо'])
            self.settings_page.do_click(element['Кнопка хорошо'])

        with allure.step('Нажать Войти'):
            element = elements['Страница авторизации']
            self.authorization_page.do_click(element['Кнопка войти'])

        with allure.step('В поле никнейм ввести никнейм пользователя'):
            element = elements['Страница логина']
            self.authorization_page.field_send_keys(element['Поле логин'], text=username)

        with allure.step('В поле пароль ввести пароль'):
            self.authorization_page.field_send_keys(element['Поле пароль'], text=User.PASSWORD)

        with allure.step('Нажать кнопку Войти'):
            self.authorization_page.do_click(element['Кнопка войти'])

        with allure.step('Проверить, что появилось уведомление для пользователя'):
            self.assertion.is_elem_displayed(element['Уведомление аккаунт удален'])

    @allure.title('При отсутствии заблокированных пользователей отображается надпись "Список пуст"')
    @allure.description('Проверка происходит на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_if_there_are_no_blocked_users_the_message_list_is_empty_is_displayed(self, elements, login_to_app):
        with allure.step('Нажать кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку редактирования профиля'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать "Редактировать профиль"'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Редактировать профиль'])

        with allure.step('Нажать "Заблокированные пользователи"'):
            element = elements['Страница редактировать профиль']
            self.edit_profile_page.do_click(element['Заблокированные пользователи'])

        with allure.step('Проверить, что список пуст и отображается надпись "Список пуст"'):
            element = elements['Страница заблокированные пользователи']
            self.assertion.is_elem_displayed(element['Список пуст'])
            self.assertion.text_in_element(element['Список пуст'], expected_text='Список пуст')

    @allure.title('Просмотр списка заблокированных пользователей')
    @allure.description('Проверка происходит на пользователе Aleska, после теста разблокируются пользователи')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_view_the_list_of_blocked_users(self, login_to_app, elements):
        with allure.step('Заблокировать пользователя Ekaterina_Fesan'):
            self.another_user_page.blocking_user_for_username('Ekaterina_Fesan')

        with allure.step('Заблокировать пользователя biryukovadariaa'):
            self.another_user_page.blocking_user_for_username('biryukovadariaa')

        with allure.step('Открыть страницу заблокированные пользователи'):
            self.blocklist_page.open()

        with allure.step('Проверить, что список заблокированных пользователей 2'):
            element = elements['Страница заблокированные пользователи']
            self.assertion.length_elements(element['Список заблокированных пользователей'], length=2)

        with allure.step('Разблокировать всех пользователей'):
            self.another_user_page.unblocking_all_users()

    @allure.title('Разблокировка пользователя')
    @allure.description('Проверка происходит на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_unblocking_user(self, elements, login_to_app):
        with allure.step('Заблокировать пользователя Ekaterina_Fesan'):
            self.another_user_page.blocking_user_for_username('Ekaterina_Fesan')

        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на кнопку бургер-меню'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать "Редактировать профиль"'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Редактировать профиль'])

        with allure.step('Нажать заблокированные пользователи'):
            element = elements['Страница редактировать профиль']
            self.edit_profile_page.do_click(element['Заблокированные пользователи'])

        with allure.step('Нажать кнопку разблокировать напротив пользователя'):
            element = elements['Страница заблокированные пользователи']
            self.blocklist_page.do_click(element['Кнопка разблокировать'])

        with allure.step('Проверить, что список пуст и отображается надпись "Список пуст"'):
            self.assertion.is_elem_displayed(element['Список пуст'])
            self.assertion.text_in_element(element['Список пуст'], expected_text='Список пуст')

    @allure.title('Добавление аватара / изменение аватара')
    @allure.description('Проверка происходит на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_add_and_change_avatar(self, elements, login_to_app):
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Запомнить ссылку на аватар пользователя'):
            element = elements['Профиль пользователя']
            old_att = self.profile_page.get_element_attribute(element['Аватар'], atr_value='src')

        with allure.step('Нажать на бургер-меню'):
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Нажать редактировать профиль'):
            element = elements['Поп ап бургер-меню профиля']
            self.profile_page.do_click(element['Редактировать профиль'])

        with allure.step('Добавить изображение в Кнопку добавить аватар'):
            element = elements['Страница редактировать профиль']
            self.edit_profile_page.input_file(element['Кнопка добавить аватар'])

        with allure.step('Нажать кнопку Хорошо'):
            self.edit_profile_page.do_click(element['Кнопка хорошо'])

        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Запомнить новую ссылку на аватар и сравнить со старой'):
            element = elements['Профиль пользователя']
            time.sleep(3)  # Не придумал как победить по другому
            self.profile_page.refresh()
            new_att = self.profile_page.get_element_attribute(element['Аватар'], atr_value='src')
            assert old_att != new_att
