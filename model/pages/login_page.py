from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.links import Links
from data.locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    def input_username_field(self, login: str):
        element = self.find_element(LoginPageLocators.FIELD_USERNAME)
        element.send_keys(login)

    def input_password_field(self, password: str):
        element = self.find_element(LoginPageLocators.FIELD_PASSWORD)
        element.send_keys(password)

    def validation_message_username_field(self, text, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(
            LoginPageLocators.VALIDATION_MESSAGE_USERNAME_FIELD, text))

    def click_signin_button(self):
        element = self.find_element(LoginPageLocators.BUTTON_SIGN_IN)
        self.do_click(element)

    def click_back_button(self):
        element = self.find_element(LoginPageLocators.BUTTON_BACK)
        self.do_click(element)

    def click_forgot_password_button(self):
        element = self.find_element(LoginPageLocators.BUTTON_FORGO_PASSWORD)
        self.do_click(element)

    def check_popup_auth_error_visible(self, text, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(
            LoginPageLocators.POPUP_AUTH_ERROR, text))
