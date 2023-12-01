from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.links import Links
from data.locators import AuthorizationPageLocators
from .base_page import BasePage


class AuthorizationPage(BasePage):
    PAGE_URL = Links.AUTHORIZATION_PAGE

    def click_sign_in_button(self):
        elem = self.find_element(AuthorizationPageLocators.BUTTON_SIGN_IN)
        self.do_click(elem)
