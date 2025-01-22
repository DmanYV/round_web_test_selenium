import time

from faker import Faker

from config.links import Links
from base.base_test import BaseTest
from fixtures.fixtures_for_subscription_tests import *
from fixtures.fixtures_for_registration_tests import registration_user


fake = Faker()


@allure.feature('Профиль пользователя')
@pytest.mark.profile
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
    @allure.severity('Minor')
    @pytest.mark.regression
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
    @allure.severity('Minor')
    @pytest.mark.regression
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
    @allure.severity('Minor')
    @pytest.mark.regression
    def test_the_ability_to_view_the_detailed_achievement_screen(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать первую ачивку в списке'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Блок ачивок'])

        with allure.step('Проверить, что открылось модальное окно с описанием ачивки'):
            element = elements['Банк ачивок']
            self.assertion.is_elem_displayed(element['Модальное окно ачивки'])

    @allure.title('Проверка возможности просмотреть у кого есть такие же ачивки')
    @allure.description('Проверка происходит на пользователе Aleska у которого есть ачивки')
    @allure.severity('Minor')
    @pytest.mark.regression
    def test_the_ability_to_view_other_users_with_similar_achievements(self, elements, login_to_app):
        with allure.step('Перейти в профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на первую ачивку'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Блок ачивок'])

        with allure.step('Нажать на аватары пользователей у которых есть эта ачивка'):
            element = elements['Модальное окно ачивки']
            self.profile_page.do_click(element['Аватары у кого есть эта ачивка'])

        with allure.step('Проверить, что открылась страница с названием "У кого есть ачивка"'):
            element = elements['Общие']
            self.assertion.text_in_element(element['Заголовок страницы'], expected_text='У кого есть ачивка')

    @allure.title('Проверка возможности открыть меню профиля')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_opportunities_to_open_the_profile_menu(self, elements, login_to_app):
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Проверяем, что поп ап не отображается и нажимаем на кнопку бургер-меню'):
            element = elements['Профиль пользователя']
            self.assertion.is_elem_invisible(element['Поп ап бургер-меню'])
            self.profile_page.do_click(element['Кнопка бургер-меню'])

        with allure.step('Проверить, что открылся поп ап'):
            self.assertion.is_elem_displayed(element['Поп ап бургер-меню'])

    @allure.title('Проверка возможности подписаться')
    @allure.description('После проверки, отписываемся от пользователя для приведения в исходное состояние')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_opportunities_to_subscribe(self, elements, login_to_app):
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Запомнить количество подписчиков'):
            element = elements['Профиль пользователя']
            subscribers = int(self.profile_page.get_element_text(element['Подписки']))

        with allure.step('Подписаться на первого пользователя'):
            self.subscription_page.subscribe_user()

        with allure.step('Проверить, что на экране появилась галочка'):
            element = elements['Страница подписки']
            self.assertion.is_elem_displayed(element['Значок галочки'])

        with allure.step('Нажать кнопку профиля'):
            self.app.profile_button_click()

        with allure.step('Проверить, что количество подписчиков увеличилось на 1'):
            element = elements['Профиль пользователя']
            self.profile_page.get_element_text(element['Подписки'])
            self.assertion.text_in_element(element['Подписки'], expected_text=str(subscribers + 1))

        with allure.step('Отписаться от пользователя'):
            self.subscription_page.unsubscribe_user()

    @allure.title('Проверка возможности отписаться')
    @allure.description('Перед проверкой проводится подписка на первого пользователя в списке')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_opportunities_to_unsubscribe(self, elements, registration_user, subscribe_user):
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать заполню позже'):
            element_profile = elements['Профиль пользователя']
            self.profile_page.do_click(element_profile['Кнопка заполню позже'])

        with allure.step('Запомнить количество подписчиков'):
            time.sleep(3)
            self.assertion.text_in_element(element_profile['Подписки'], expected_text= '1')

        with allure.step('Отписаться от пользователя'):
            self.subscription_page.unsubscribe_user()

        with allure.step('Проверить, что на экране появилась галочка'):
            element = elements['Страница подписки']
            self.assertion.is_elem_displayed(element['Значок галочки'])

        with allure.step('Нажать кнопку профиля'):
            self.app.profile_button_click()

        with allure.step('Нажать заполню позже'):
            self.profile_page.do_click(element_profile['Кнопка заполню позже'])

        with allure.step('Проверить, что количество подписчиков не изменилось'):
            time.sleep(3)
            self.assertion.text_in_element(element_profile['Подписки'], expected_text='0')

    @allure.title('Проверка возможности посмотреть список своих подписчиков')
    @allure.description('Проверка происходит на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_opportunities_to_see_the_list_of_your_subscribers(self, elements, login_to_app):
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на Подписчики'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Подписчики'])

        with allure.step('Проверить, что список подписчиков >= 1'):
            element = elements['Страница подписки']
            self.assertion.length_elements(element['Список пользователей'], length=1)

    @allure.title('Проверка возможности посмотреть список своих подписок')
    @allure.description('Проверка происходит на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_opportunities_to_see_the_list_of_your_subscriptions(self, elements, login_to_app):
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()

        with allure.step('Нажать на Подписки'):
            element = elements['Профиль пользователя']
            self.profile_page.do_click(element['Подписки'])

        with allure.step('Проверить, что список подписок >= 3'):
            element = elements['Страница подписки']
            self.assertion.length_elements(element['Список пользователей'], length=3)

    @allure.title('Проверка возможности перейти в профиль другого пользователя')
    @allure.description('Проверка происходит на пользователе Aleska, открывается пользователь Natalya')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_opportunities_to_go_to_another_user_profile(self, elements, login_to_app):
        element_profile_page = elements['Профиль пользователя']
        element_subscription_page = elements['Страница подписки']
        element_global_searching_page = elements['Глобальный поиск']
        with allure.step('Нажать на кнопку профиль'):
            self.app.profile_button_click()
        with allure.step('Нажать на Подписки'):
            self.profile_page.do_click(element_profile_page['Подписки'])
        with allure.step('Нажать "Глобальный поиск"'):
            self.subscription_page.do_click(element_subscription_page['Кнопка глобальный поиск'])
        with allure.step('В поле поиска ввести Natalya'):
            self.global_searching_page.field_send_keys(element_global_searching_page['Поисковое поле'], text='Natalya')
        with allure.step('Найти в списке Natalya и перейти в профиль'):
            self.subscription_page.search_by_username('Natalya')
        with allure.step('Проверить, что открылась страница пользователя Natalya'):
            self.assertion.page_is_opened(Links.PROFILE_PAGE + '/Natalya')
