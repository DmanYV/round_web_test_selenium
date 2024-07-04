import time

from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from config.locators import AllPageLocators


class Assertion(BasePage):
    def text_in_element(self, element_locator: tuple, expected_text: str):
        """
        Проверка совпадения текста элемента

        :param element_locator:
            локатор элемента
        :param expected_text:
            ожидаемый текст

        """
        actual_text = self.find_element(element_locator).text
        assert expected_text == actual_text, f"Ожидался текст: '{expected_text}', отображается текс: '{actual_text}'"

    def page_is_opened(self, page_url):
        """
        Функция проверка, что запрашиваемая страница открыта

        :param page_url:
            url страницы

        """
        self.element_is_not_visible(AllPageLocators.SPINNER)
        assert self.wait.until(EC.url_to_be(page_url))

    def is_elem_displayed(self, by_locator: tuple, wait_time: int = 1) -> bool:
        """
        Проверка отображения элемента на странице

        :param by_locator:
            локатор элемента

        :param wait_time:
            лимит ожидания

        """

        time.sleep(wait_time)
        if self.find_element(by_locator):
            return self.find_element(by_locator).is_displayed()
        else:
            return False

    def is_elem_enabled(self, by_locator, wait_time=4) -> bool:
        """
        Проверка доступности элемента

        :param by_locator:
            локатор элемента

        :param wait_time:
            время ожидания

        """

        element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
        time.sleep(0.5)
        if element.is_enabled():
            return True
        else:
            return False

