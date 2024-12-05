from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.links import Links


class RubricPage(BasePage):
    PAGE_URL = Links.RUBRIC_PAGE

    def select_interest_by_name(self, interest_name):
        """
        Выбор Интереса по названию

        :param interest_name: Название интереса

        """

        interest = self.find_element(
            (By.XPATH, f'//div[contains(@class,"rubrics_chips")][contains(.,"{interest_name}")]'))
        self.do_click(interest)
