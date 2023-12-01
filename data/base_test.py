import pytest

from model.pages.authorization_page import AuthorizationPage
from model.pages.login_page import LoginPage


class BaseTest:
    authorization_page: AuthorizationPage
    login_page: LoginPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        driver = driver
        request.cls.authorization_page = AuthorizationPage(driver)
        request.cls.login_page = LoginPage(driver)
