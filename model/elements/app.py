import config.locators
from config.links import Links
from base.base_page import BasePage


class App(BasePage):
    PAGE_URL = Links.MAIN_PAGE

    def main_button_click(self):
        """
        Клик по кнопке главная в панели навигации
        """

        self.do_click(config.locators.AppNavigationLocators.locators['Кнопка главная'])

    def feed_button_click(self):
        """
        Клик по кнопке лента в панели навигации
        """

        self.do_click(config.locators.AppNavigationLocators.locators['Кнопка лента'])

    def newbie_button_click(self):
        """
        Клик по кнопке новичка в панели навигации
        """

        self.do_click(config.locators.AppNavigationLocators.locators['Кнопка плюс'])

    def profile_button_click(self):
        """
        Клик по кнопке профиль в панели навигации
        """

        self.do_click(config.locators.AppNavigationLocators.locators['Кнопка профиль'])

    def notification_button_click(self):
        """
        Клик по кнопке уведомления в панели навигации
        """

        self.do_click(config.locators.AppNavigationLocators.locators['Кнопка уведомления'])
