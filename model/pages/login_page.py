from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.links import Links
from data.locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    def field_username_input(self, text: str):
        elem = self.find_element(LoginPageLocators.FIELD_USERNAME)
        elem.send_keys(text)

    def field_password_input(self, text: str):
        elem = self.find_element(LoginPageLocators.FIELD_PASSWORD)
        elem.send_keys(text)

    def button_signin_click(self):
        elem = self.find_element(LoginPageLocators.BUTTON_SIGN_IN)
        self.do_click(elem)

