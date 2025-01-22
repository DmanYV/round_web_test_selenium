from base.base_page import BasePage
from model.elements.app import App
from config.links import Links


class ChallengePage(BasePage):
    PAGE_URL = Links.CHALLENGE_PAGE

    def __init__(self, driver):
        super().__init__(driver)
        self.app = App(driver)