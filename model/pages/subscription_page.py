from selenium.webdriver.common.by import By

import config.locators
from base.base_page import BasePage
from model.elements.app import App


class SubscriptionPage(BasePage):
    PAGE_URL = None

    def __init__(self, driver):
        super().__init__(driver)
        self.app = App(driver)

    def subscribe_user(self):
        """
        Подписка на первого пользователя в списке

        """
        self.app.profile_button_click()
        self.do_click(config.locators.ProfilePageLocators.locators['Подписки'])
        self.do_click(config.locators.SubscriptionPageLocators.locators['Все пользователи'])
        elem = self.find_element(config.locators.SubscriptionPageLocators.locators['Подписка на первого пользователя'])
        self.do_click(elem)

    def unsubscribe_user(self):
        """
        Отписка от перового пользователя в списке

        """
        self.app.profile_button_click()
        self.do_click(config.locators.ProfilePageLocators.locators['Подписки'])
        elem = self.find_element(config.locators.SubscriptionPageLocators.locators['Отписка от первого пользователя'])
        self.do_click(elem)

    def search_by_username(self, username):
        """
        Поиск пользователя в списке по имени и переходе в его профиль

        :param username: Имя пользователя

        """
        user = self.find_element(
            (By.XPATH, f'//div[contains(@class,"user-block_wrapper-name")][contains(.,"{username}")]'))
        self.do_click(user)
