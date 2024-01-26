from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from data.links import Links
from data.locators import LoginPageLocators


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    def field_username_input(self, login: str):
        element = self.find_element(LoginPageLocators.FIELD_USERNAME)
        element.send_keys(login)

    def field_password_input(self, password: str):
        element = self.find_element(LoginPageLocators.FIELD_PASSWORD)
        element.send_keys(password)

    def field_username_validation_message(self, text, wait_time=10):
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

    def check_popup_auth_error_visible(self, text, wait_time=10):
        text_ = WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(
            LoginPageLocators.POPUP_AUTH_ERROR, text))
        assert text_ == text
