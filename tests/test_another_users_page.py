import allure
import pytest
from faker import Faker

from base.base_test import BaseTest

from fixtures.fixtures_for_registration_tests import registration_user
fake = Faker()
fakeru = Faker("ru_RU")


@allure.feature('Профиль другого пользователя')
@pytest.mark.another_users_page
class TestAnotherUsersPage(BaseTest):
    @allure.title('Проверить, есть возможность подписаться на пользователя')
    @allure.description('Подписываемся на пользователя из профиля и после отписываемся. '
                        'Проверка на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_of_the_ability_to_subscribe_to_a_user_from_his_profile(self, elements, login_to_app):
        with allure.step('Открыть свой профиль'):
            self.app.profile_button_click()

        with allure.step('Запомнить количество подписок'):
            element = elements['Профиль пользователя']
            initial_subscriptions_count = int(self.profile_page.get_element_text(element['Подписки']))

        with allure.step('Открыть страницу пользователя "Daaniaa"'):
            self.another_user_page.subscribe_user_for_username(username='Daaniaa')

        with allure.step('Проверить, что появилась галочка на экране'):
            element = elements['Страница другого пользователя']
            self.assertion.is_elem_displayed(element['Значок галочки'])

        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Проверить, что количество подписок увеличилось на 1'):
            element = elements['Профиль пользователя']
            self.assertion.text_in_element(element['Подписки'], str(initial_subscriptions_count + 1))

        with allure.step('Отписываемся от пользователя "Daaniaa"'):
            self.another_user_page.unsubscribe_user_for_username('Daaniaa')

    @allure.title('Проверить, есть возможность отписаться от пользователя')
    @allure.description('Подписываемся на пользователя из профиля и после отписываемся. '
                        'Проверка на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_ability_to_unsubscribe_from_a_users_profile(self, elements, login_to_app):
        with allure.step('Подписаться на пользователя "Serg1206"'):
            self.another_user_page.subscribe_user_for_username('Serg1206')

        with allure.step('Нажать кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Запомнить количество подписок'):
            element = elements['Профиль пользователя']
            initial_subscriptions_count = int(self.profile_page.get_element_text(element['Подписки']))

        with allure.step('Отписаться от пользователя "Serg1206"'):
            self.another_user_page.unsubscribe_user_for_username('Serg1206')

        with allure.step('Проверить, что появилась галочка на экране'):
            element = elements['Страница другого пользователя']
            self.assertion.is_elem_displayed(element['Значок галочки'])

        with allure.step('Нажать кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Проверить, что количество подписок уменьшилось на 1'):
            element = elements['Профиль пользователя']
            self.assertion.text_in_element(element['Подписки'], str(initial_subscriptions_count - 1))

    @pytest.mark.parametrize('options', [
        'Спам',
        'Нарушение авторского права, неоригинальный контент',
        'Оскорбление, враждебные высказывания',
        'Материал для взрослых или действия сексуального характера',
        'Пропаганда наркотиков',
        'Продажа оружия',
        'Травля, преследование, призыв к травле или преследованию',
        'Призыв к суициду',
        'Жестокое обращение с животными',
        'Введение в заблуждение',
        'Мошенничество',
        'Насилие/экстремизм'
    ])
    @allure.title('Проверить, есть возможность пожаловаться на пользователя по причине "{options}"')
    @allure.description('Регистрируется новый пользователь и жалуется на пользователя')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_opportunities_to_report_a_user(self, elements, registration_user, options):
        with allure.step('Открыть профиль пользователя "Zina.Sozonova"'):
            self.another_user_page.open_profile('Zina.Sozonova')

        with allure.step('Нажать на три точки'):
            element = elements['Страница другого пользователя']
            self.another_user_page.do_click(element['Кнопка три точки'])

        with allure.step('Нажать Пожаловаться'):
            self.another_user_page.do_click(element['Пожаловаться'])

        with allure.step(f'Выбрать "{options}"'):
            self.checkbox.checkbox_on(element[options])

        with allure.step('Нажать кнопку Пожаловаться'):
            self.another_user_page.do_click(element['Кнопка пожаловаться'])

        with allure.step('Проверить, что появилось уведомление "Жалоба на пользователя отправлена"'):
            self.assertion.is_elem_displayed(element['Уведомление жалоба на пользователя отправлена'])

    @allure.title('Проверить, есть возможность пожаловаться на пользователя по причине "Другое"')
    @allure.description('Регистрируется новый пользователь и жалуется на пользователя по причине другое')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_opportunities_to_report_a_user_for_other_reason(self, elements, registration_user):
        with allure.step('Открыть профиль пользователя "Zina.Sozonova"'):
            self.another_user_page.open_profile('Zina.Sozonova')

        with allure.step('Нажать на три точки'):
            element = elements['Страница другого пользователя']
            self.another_user_page.do_click(element['Кнопка три точки'])

        with allure.step('Нажать Пожаловаться'):
            self.another_user_page.do_click(element['Пожаловаться'])

        with allure.step(f'Выбрать "Другое"'):
            self.checkbox.checkbox_on(element['Другое'])

        with allure.step('В поле жалобы написать текст'):
            self.another_user_page.field_send_keys(element['Поле причина жалобы'], text=fakeru.text(max_nb_chars=250))

        with allure.step('Нажать кнопку Пожаловаться'):
            self.another_user_page.do_click(element['Кнопка пожаловаться'])

        with allure.step('Проверить, что появилось уведомление "Жалоба на пользователя отправлена"'):
            self.assertion.is_elem_displayed(element['Уведомление жалоба на пользователя отправлена'])

    @allure.title('Проверить, данные заблокированного пользователя не отображаются (проекты/подписки/ачивки/аватар)')
    @allure.description('Проверяется на новом пользователи, блокируется пользователь Evelinkaaa')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_the_data_of_the_blocked_user_is_not_displayed(self, elements, registration_user):

        with allure.step('Заблокировать пользователя Evelinkaaa'):
            self.another_user_page.blocking_user_for_username('Evelinkaaa')

        with allure.step('Обновить страницу'):
            self.another_user_page.refresh()

        with allure.step('Проверить, что не видны проекты пользователя'):
            self.assertion.is_elem_invisible(elements['Страница другого пользователя']['Список проектов'])

        with allure.step('Проверить, что подписки отображает как 0'):
            self.assertion.text_in_element(elements['Страница другого пользователя']['Подписки'], expected_text='0')

        with allure.step('Проверить, что блок ачивок не видим'):
            self.assertion.is_elem_invisible(elements['Страница другого пользователя']['Блок ачивок'])

        with allure.step('Проверить, что аватар не виден'):
            self.assertion.is_elem_invisible(elements['Страница другого пользователя']['Аватар'])

    @allure.title('Проверить, заблокированный пользователь не может просматривать профиль заблокировавшего пользователя')
    @allure.description('Пользователь Dina заблокировала Aleska, тест проводится на Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_the_blocked_user_cannot_view_the_profile_of_the_blocked_user(self, elements, login_to_app):
        with allure.step('Открыть профиль пользователя Dina'):
            self.another_user_page.open_profile('Dina')

        with allure.step('Проверить, что не видны проекты пользователя'):
            self.assertion.is_elem_invisible(elements['Страница другого пользователя']['Список проектов'])

        with allure.step('Проверить, что подписки отображает как 0'):
            self.assertion.text_in_element(elements['Страница другого пользователя']['Подписки'], expected_text='0')

        with allure.step('Проверить, что блок ачивок не видим'):
            self.assertion.is_elem_invisible(elements['Страница другого пользователя']['Блок ачивок'])

        with allure.step('Проверить, что аватар не виден'):
            self.assertion.is_elem_invisible(elements['Страница другого пользователя']['Аватар'])

    @allure.title('Проверить, есть возможность разблокировать пользователя')
    @allure.description('Тест проводится на Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_it_is_possible_to_unblock_the_user(self, elements, login_to_app):
        with allure.step('Заблокировать пользователя "Vika."'):
            self.another_user_page.blocking_user_for_username('Vika.')

        with allure.step('Проверить, что отображается "Пользователь заблокирован"'):
            element = elements['Страница другого пользователя']
            self.assertion.is_elem_displayed(element['Пользователь заблокирован'])

        with allure.step('Нажать 3 точки'):
            self.another_user_page.do_click(element['Кнопка три точки'])

        with allure.step('Нажать Разблокировать'):
            self.another_user_page.do_click(element['Разблокировать'])

        with allure.step('Проверить, что появился список проектов'):
            self.assertion.is_elem_displayed(element['Список проектов'])

    @allure.title('Проверить, есть возможность просматривать ачивки пользователя')
    @allure.description('Тест проводится на Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_possible_to_view_the_users_achievements(self, elements, login_to_app):
        with allure.step('Открыть страницу "Ennis"'):
            self.another_user_page.open_profile('Ennis')

        with allure.step('Проверить, что блок с ачивками видим'):
            element = elements['Страница другого пользователя']
            self.assertion.is_elem_displayed(element['Блок ачивок'])

    @allure.title('Проверить, есть возможность просматривать проекты пользователя')
    @allure.description('Тест проводится на Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_it_is_possible_to_view_the_users_projects(self, elements, login_to_app):
        with allure.step('Открыть страницу "Polina_04"'):
            self.another_user_page.open_profile('Polina_04')

        with allure.step('Проверить, что список проектов видим'):
            element = elements['Страница другого пользователя']
            self.assertion.is_elem_displayed(element['Список проектов'])
