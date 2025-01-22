from base.base_page import BasePage
from model.elements.app import App
from config.links import Links


class GlobalSearchingPage(BasePage):
    PAGE_URL = Links.GLOBAL_SEARCHING_PAGE

    def __init__(self, driver):
        super().__init__(driver)
        self.app = App(driver)