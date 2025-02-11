from selenium.webdriver.common.by import By

from base.base_page import BasePage


class Chips(BasePage):
    """ Класс, описывающий действия с чипсами на страницах """

    def select_chip(self, chip_name):
        """
        Выбор чипса из списка

        :param chip_name: Название чипса
        :return:
        """

        chip_locator = (By.XPATH, f'//span[@data-testing="chip_rubrics"]-[contains(.,"{chip_name}")]')
        chip = self.find_element(chip_locator)
        self.do_click(chip)
