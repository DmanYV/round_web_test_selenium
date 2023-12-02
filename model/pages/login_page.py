from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.links import Links
from data.locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    def field_username_input(self, text: str):
        element = self.find_element(LoginPageLocators.FIELD_USERNAME)
        element.send_keys(text)

    def field_password_input(self, text: str):
        element = self.find_element(LoginPageLocators.FIELD_PASSWORD)
        element.send_keys(text)

    def validation_message_username_field(self, text, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(
            LoginPageLocators.VALIDATION_MESSAGE_USERNAME_FIELD, text))

    def button_signin_click(self):
        element = self.find_element(LoginPageLocators.BUTTON_SIGN_IN)
        self.do_click(element)

    def button_back_click(self):
        element = self.find_element(LoginPageLocators.BUTTON_BACK)
        self.do_click(element)

    def button_forgot_password_click(self):
        element = self.find_element(LoginPageLocators.BUTTON_FORGO_PASSWORD)
        self.do_click(element)

