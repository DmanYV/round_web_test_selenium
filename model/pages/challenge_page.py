import config.locators
from base.base_assertion import Assertion

from base.base_page import BasePage
from model.elements.app import App
from config.links import Links



class ChallengePage(BasePage):
    PAGE_URL = Links.CHALLENGE_PAGE

    def __init__(self, driver):
        super().__init__(driver)
        self.app = App(driver)
        self.assertion = Assertion(driver)
        self.element = config.locators.ChallengePageLocators.locators

    def click_favorites_button(self):
        """
        Клик по кнопке избранное

        """
        self.assertion.is_elem_displayed(self.element['Проекты участников'])
        self.do_click(self.element['Кнопка избранное'])