import allure
import pytest
import config.locators

from model.elements.app import App


@pytest.fixture(scope='function')
@allure.step('Подписка на пользователя первого в писке')
def subscribe_user(driver):
    app = App(driver)
    app.profile_button_click()
    app.do_click(config.locators.ProfilePageLocators.locators['Подписки'])
    app.do_click(config.locators.SubscriptionPageLocators.locators['Все пользователи'])
    elem = app.find_element(config.locators.SubscriptionPageLocators.locators['Подписка на первого пользователя'])
    app.do_click(elem)


@pytest.fixture(scope='function')
@allure.step('Отписка от пользователя')
def unsubscribe_user(request, driver):
    yield driver
    app = App(driver)
    app.profile_button_click()
    app.do_click(config.locators.ProfilePageLocators.locators['Подписки'])
    app.do_click(config.locators.SubscriptionPageLocators.locators['Отписка от первого пользователя'])

