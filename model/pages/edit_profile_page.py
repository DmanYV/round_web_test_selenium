import config.locators
from config.links import Links
from base.base_page import BasePage
from model.elements.app import App
from model.pages.profile_page import ProfilePage


class EditProfilePage(BasePage):
    PAGE_URL = Links.EDIT_PROFILES_PAGE

    def __init__(self, driver):
        super().__init__(driver)
        self.app = App(driver)
        self.profile_page = ProfilePage(driver)

    def change_username(self, username: str):
        self.app.profile_button_click()

        self.profile_page.do_click(config.locators.ProfilePageLocators.locators['Кнопка бургер-меню'])
        self.profile_page.do_click(config.locators.PopUpBurgerMenuProfileLocators.locators['Редактировать профиль'])
        self.clear(config.locators.EditProfileLocators.locators['Поле никнейм'])
        self.field_send_keys(config.locators.EditProfileLocators.locators['Поле никнейм'], text=username)
        self.scroll_to_element(config.locators.EditProfileLocators.locators['Кнопка сохранить'])
        self.do_click(config.locators.EditProfileLocators.locators['Кнопка сохранить'])
