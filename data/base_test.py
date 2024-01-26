import pytest

from model.pages.authorization_page import AuthorizationPage
from model.pages.login_page import LoginPage
from model.pages.main_page import MainPage
from model.pages.rubric_page import RubricPage


class BaseTest:
    authorization_page: AuthorizationPage
    login_page: LoginPage
    main_page: MainPage
    rubric_page: RubricPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        driver = driver
        request.cls.authorization_page = AuthorizationPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.rubric_page = RubricPage(driver)
