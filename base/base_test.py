import pytest

from model.pages.authorization_page import AuthorizationPage
from model.pages.login_page import LoginPage
from model.pages.main_page import MainPage
from model.pages.rubric_page import RubricPage
from settings import User

from model.api.authorization import ApiAuthorization


class BaseTest:
    User: User
    authorization_page: AuthorizationPage
    login_page: LoginPage
    main_page: MainPage
    rubric_page: RubricPage
    api_authorization: ApiAuthorization

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        driver = driver
        request.cls.User = User()
        request.cls.authorization_page = AuthorizationPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.rubric_page = RubricPage(driver)
        request.cls.api_authorization = ApiAuthorization(driver)
