import allure

import config.locators
from base.base_assertion import Assertion

from base.base_page import BasePage
from config.links import Links
from model.elements.app import App


class AnotherUserPage(BasePage):
    PAGE_URL = Links.BLOCK_LIST_PAGE

    def __init__(self, driver):
        super().__init__(driver)
        self.app = App(driver)
        self.assertion = Assertion(driver)

    def blocking_user_for_username(self, username: str):
        """
        Метод добавления пользователя в список заблокированные пользователи.

        :param:
            Username (str):
                Имя пользователя которого надо заблокировать.

        """
        self.driver.get(Links.PROFILE_PAGE + f'/{username}')
        self.app.do_click(config.locators.AnotherUserPageLocators.locators['Кнопка три точки'])
        self.app.do_click(config.locators.AnotherUserPageLocators.locators['Заблокировать'])
        self.assertion.is_elem_displayed(config.locators.AnotherUserPageLocators.locators['Пользователь заблокирован'])

    def unblocking_user_for_username(self, username: str):
        """
        Метод удаления пользователя из списка заблокированные пользователи.

        :param:
            Username (str):
                Имя пользователя которого надо разблокировать.

        """
        self.driver.get(Links.PROFILE_PAGE + f'/{username}')
        self.app.do_click(config.locators.AnotherUserPageLocators.locators['Кнопка три точки'])
        self.app.do_click(config.locators.AnotherUserPageLocators.locators['Разблокировать'])
        self.assertion.is_elem_invisible(config.locators.AnotherUserPageLocators.locators['Пользователь заблокирован'])

    def unblocking_all_users(self):
        """
        Метод разблокировки всех пользователей из списка заблокированных пользователей.

        """
        with allure.step('Открыть страницу Заблокированный пользователи'):
            self.open()

        with allure.step('Нажать кнопку Разблокировать у всех пользователей'):
            lists = self.find_elements(config.locators.BlockListPageLocators.locators['Кнопка разблокировать'])
            for click in lists:
                click.click()

    def subscribe_user_for_username(self, username):
        """
        Подписка на пользователя по имени

        :param username: Имя пользователя

        """
        self.driver.get(Links.PROFILE_PAGE + f'/{username}')
        self.app.do_click(config.locators.AnotherUserPageLocators.locators['Кнопка подписаться'])

    def unsubscribe_user_for_username(self, username):
        """
        Отписка от пользователя по имени

        :param username: Имя пользователя

        """
        self.driver.get(Links.PROFILE_PAGE + f'/{username}')
        self.app.do_click(config.locators.AnotherUserPageLocators.locators['Кнопка подписка'])

    def open_profile(self, username):
        """
        Открыть профиль пользователя по имени

        :param username: Имя пользователя

        """
        self.driver.get(Links.PROFILE_PAGE + f'/{username}')
