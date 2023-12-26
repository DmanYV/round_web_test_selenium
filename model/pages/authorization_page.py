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

    def click_close_button(self):
        close = self.find_element(AuthorizationPageLocators.BUTTON_CLOSE)
        self.do_click(close)

    def click_carrot_quest_button(self):
        carrot = self.find_element(AuthorizationPageLocators.BUTTON_CARROT_QUEST)
        self.do_click(carrot)

    def click_sms_login_button(self):
        sms = self.find_element(AuthorizationPageLocators.BUTTON_SMS_LOGIN)
        self.do_click(sms)

    def click_vk_login_button(self):
        vk = self.find_element(AuthorizationPageLocators.BUTTON_VK_LOGIN)
        self.do_click(vk)

    def click_email_login_button(self):
        email = self.find_element(AuthorizationPageLocators.BUTTON_EMAIL_LOGIN)
        self.do_click(email)

    def click_licensed_shelf(self):
        licensed = self.find_element(AuthorizationPageLocators.BUTTON_LICENSED_SHELF)
        self.do_click(licensed)
