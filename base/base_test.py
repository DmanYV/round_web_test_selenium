import pytest

from base.base_assertion import Assertion
from model.pages.authorization_page import AuthorizationPage
from model.pages.login_page import LoginPage
from model.pages.main_page import MainPage
from model.pages.rubric_page import RubricPage
from model.pages.join_page import JoinPage
from model.pages.reset_password_page import ResetPasswordPage
from model.pages.profile_page import ProfilePage
from settings import User
from settings import MetaBaseUser

from model.api.authorization import ApiAuthorization
from model.api.metabase import MetaBase
from model.elements.app import App


class BaseTest:
    User: User
    MetaBaseUser: MetaBaseUser
    assertion: Assertion
    authorization_page: AuthorizationPage
    join_page: JoinPage
    login_page: LoginPage
    reset_password_page: ResetPasswordPage
    main_page: MainPage
    rubric_page: RubricPage
    profile_page: ProfilePage
    api_authorization: ApiAuthorization
    metabase: MetaBase
    app: App

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        driver = driver
        request.cls.User = User()
        request.cls.MetaBaseUser = MetaBaseUser()
        request.cls.app = App(driver)
        request.cls.assertion = Assertion(driver)
        request.cls.authorization_page = AuthorizationPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.reset_password_page = ResetPasswordPage(driver)
        request.cls.join_page = JoinPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.rubric_page = RubricPage(driver)
        request.cls.profile_page = ProfilePage(driver)
        request.cls.api_authorization = ApiAuthorization(driver)
        request.cls.metabase = MetaBase(driver)
