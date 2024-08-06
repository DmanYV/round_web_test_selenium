import time

from base.base_page import BasePage


class Checkbox(BasePage):
    """ Класс, описывающий действия с чекбоксами на страницах """

    def checkbox_on(self, by_locator: tuple, wait_time: int = 1):
        """
        Проверяет включен ли чекбокс. Если выключен, то включает его

        :param by_locator:
            локатор чекбокса

        :param wait_time:
            время ожидания

        """
        time.sleep(wait_time)
        checkbox = self.find_element(by_locator)
        match checkbox.is_selected():
            case True:
                pass
            case False:
                checkbox.click()

        return self

    def checkbox_off(self, by_locator: tuple, wait_time: int = 1):
        """
        Проверяет выключен ли чекбокс. Если включен, то выключает его

        :param by_locator:
            локтор чекбокса

        :param wait_time:
            время ожидания

        """

        time.sleep(wait_time)
        checkbox = self.find_element(by_locator)
        match checkbox.is_selected():
            case True:
                checkbox.click()
            case False:
                pass
        return self
