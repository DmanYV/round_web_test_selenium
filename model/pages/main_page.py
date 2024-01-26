from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.pages.base_page import BasePage
from data.links import Links
from data.locators import MainPageLocators


class MainPage(BasePage):
    PAGE_URL = Links.MAIN_PAGE
