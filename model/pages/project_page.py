import config.locators
from base.base_assertion import Assertion

from base.base_page import BasePage
from config.links import Links


class ProjectPage(BasePage):
    PAGE_URL = Links.PROJECT_PAGE

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertion(driver)
        self.element = config.locators.ProjectPageLocators.locators

    def click_like_button(self):
        """
        Клик по кнопке лайка
        Проверяет, отображение интерактивной панели->
        После проверяет поставлен или нет лайк и выполняет обратное действие
        """
        self.assertion.is_elem_displayed(self.element['Интерактивная панель'])
        try:
            self.do_click(self.element['Кнопка убрать лайк'])
        except:
            self.do_click(self.element['Кнопка лайк'])
