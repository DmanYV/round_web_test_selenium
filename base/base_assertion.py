from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from config.locators import AllPageLocators


class Assertion(BasePage):
    """Проверка, что текст элемента соответствует проверяемому"""
    def text_in_element(self, element_locator: tuple, expected_text: str):
        actual_text = self.find_element(element_locator).text
        assert expected_text == actual_text, f"Ожидался текст: '{expected_text}', отображается текс: '{actual_text}'"

    def page_is_opened(self, page_url):
        """Функция проверка, что запрашиваемая страница открыта"""
        self.element_is_not_visible(AllPageLocators.SPINNER)
        assert self.wait.until(EC.url_to_be(page_url))
