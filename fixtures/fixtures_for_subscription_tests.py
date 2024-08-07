import allure
import pytest
import config.locators

from model.elements.app import App


@pytest.fixture(scope='function')
@allure.title('Подписка на пользователя первого в списке')
@allure.step('Подписка на пользователя первого в списке')
def subscribe_user(driver):
    """ Подписка на первого пользователя в списке """
    app = App(driver)
    app.profile_button_click()
    app.do_click(config.locators.ProfilePageLocators.locators['Подписки'])
    app.do_click(config.locators.SubscriptionPageLocators.locators['Все пользователи'])
    elem = app.find_element(config.locators.SubscriptionPageLocators.locators['Подписка на первого пользователя'])
    app.do_click(elem)


@pytest.fixture(scope='function')
@allure.title('Отписка от первого пользователя в списке')
@allure.step('Отписка от первого пользователя в списке')
def unsubscribe_user(request, driver):
    """ Отписка от первого пользователя в списке """
    yield driver
    app = App(driver)
    app.profile_button_click()
    app.do_click(config.locators.ProfilePageLocators.locators['Подписки'])
    app.do_click(config.locators.SubscriptionPageLocators.locators['Отписка от первого пользователя'])

