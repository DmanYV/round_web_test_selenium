import pytest

from base.base_assertion import Assertion
from model.pages.authorization_page import AuthorizationPage
from model.pages.login_page import LoginPage
from model.pages.main_page import MainPage
from model.pages.rubric_page import RubricPage
from model.pages.join_page import JoinPage
from model.pages.reset_password_page import ResetPasswordPage
from model.pages.profile_page import ProfilePage
from model.pages.invitation_page import InvitationPage
from model.pages.favorite_projects_page import FavoriteProjectsPage
from model.pages.favorite_challenge_page import FavoriteChallengePage
from model.pages.edit_profile_page import EditProfilePage
from model.pages.subscription_page import SubscriptionPage
from model.pages.settings_page import SettingsPage
from model.pages.blocklist_page import BlockListPage
from model.pages.another_user_page import AnotherUserPage
from model.pages.global_searching_page import GlobalSearchingPage

from settings import User
from settings import MetaBaseUser

from model.api.authorization import ApiAuthorization
from model.api.metabase import MetaBase

from model.elements.app import App
from model.elements.checkbox import Checkbox


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
    invitation_page: InvitationPage
    favorite_projects_page: FavoriteProjectsPage
    favorite_challenge_page: FavoriteChallengePage
    edit_profile_page: EditProfilePage
    subscription_page: SubscriptionPage
    global_searching_page: GlobalSearchingPage
    settings_page: SettingsPage
    blocklist_page: BlockListPage
    another_user_page: AnotherUserPage
    api_authorization: ApiAuthorization
    metabase: MetaBase
    app: App
    checkbox: Checkbox

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        driver = driver
        request.cls.User = User()
        request.cls.MetaBaseUser = MetaBaseUser()
        request.cls.app = App(driver)
        request.cls.checkbox = Checkbox(driver)
        request.cls.assertion = Assertion(driver)
        request.cls.authorization_page = AuthorizationPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.reset_password_page = ResetPasswordPage(driver)
        request.cls.join_page = JoinPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.rubric_page = RubricPage(driver)
        request.cls.profile_page = ProfilePage(driver)
        request.cls.invitation_page = InvitationPage(driver)
        request.cls.favorite_projects_page = FavoriteProjectsPage(driver)
        request.cls.favorite_challenge_page = FavoriteChallengePage(driver)
        request.cls.edit_profile_page = EditProfilePage(driver)
        request.cls.subscription_page = SubscriptionPage(driver)
        request.cls.global_searching_page = GlobalSearchingPage(driver)
        request.cls.settings_page = SettingsPage(driver)
        request.cls.blocklist_page = BlockListPage(driver)
        request.cls.another_user_page = AnotherUserPage(driver)
        request.cls.api_authorization = ApiAuthorization(driver)
        request.cls.metabase = MetaBase(driver)
