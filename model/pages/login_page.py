from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from config.links import Links
from config.locators import LoginPageLocators


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE
