import time

from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from config.locators import AllPageLocators


class Assertion(BasePage):
    def text_in_element(self, by_locator: tuple, expected_text: str or int):
        """
        Проверка совпадения текста элемента

        :param by_locator:
            локатор элемента
        :param expected_text:
            ожидаемый текст

        """
        time.sleep(1)
        actual_text = self.find_element(by_locator).text
        assert expected_text == actual_text, f"Ожидался текст: '{expected_text}', отображается текст: '{actual_text}'"

    def length_simbols_in_text(self, by_locator: tuple, length: int):
        """
        Функция проверки, длины текста


        :param by_locator:
            локатор текстового поля

        :param length:
            ожидаемая длина текста

        """
        actual_text_length = len(self.find_element(by_locator).text)
        assert length == actual_text_length, f"Ожидалось длина текста: {length}, текущая длина: {actual_text_length}"

    def text_in_element_length(self, by_locator: tuple, length: int):
        """
        Функция проверки, длины текста в элементе

        :param by_locator:
            локатор элемента
        :param length:
            ожидаемая длина текста

        """
        actual_text_length = len(self.find_element(by_locator).text)
        assert length == actual_text_length, f"Ожидалось длина текста: {length}, текущая длина: {actual_text_length}"

    def page_is_opened(self, page_url):
        """
        Функция проверки, что запрашиваемая страница открыта

        :param page_url:
            url страницы

        """
        self.element_is_not_visible(AllPageLocators.locators['Спиннер загрузки'])
        self.wait.until(EC.url_to_be(page_url))
        assert page_url == self.driver.current_url, \
            f'Ожидалась страница {page_url}, открылась {self.driver.current_url}'

    def is_elem_displayed(self, by_locator: tuple) -> None:
        """
        Проверка отображения элемента на странице

        :param by_locator:
            локатор элемента

        """

        assert self.find_element(by_locator).is_displayed()

    def is_elem_invisible(self, by_locator, wait_time: int = 4) -> None:
        """
        Проверка, что элемент невидим

        :param by_locator:
            локатор элемента

        :param wait_time:
            время ожидания

        """
        assert WebDriverWait(self.driver, wait_time).until(EC.invisibility_of_element_located(by_locator))

    def is_elem_enabled(self, by_locator, wait_time: int = 4) -> bool:
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

    def is_elem_attribute_matches(self, by_locator: tuple, value: str, text: str or int):
        """
        Проверка совпадения аттрибута элемента

        :param by_locator:
            локатор элемента

        :param value
            тип атрибут элемента

        :param text:
            значение атрибута

        """

        assert self.find_element(by_locator).get_attribute(value) == text, \
            f'Ожидалось значение {text}, Отображается значение {self.find_element(by_locator).get_attribute(value)}'

    def length_elements(self, by_locator: tuple, length=0) -> len:
        """
        Получение длины списка элементов на странице, ожидая, что их > 0

        :param length:
        минимальное ожидаемое количество элементов, по умолчанию 0
            количество элементов

        :param by_locator:
            локатор списка элементов

        :return:
            длина списка
        """
        assert len(self.find_elements(by_locator)) >= length, (
            f'Ожидалось элементов >= {length}, отображается {len(self.find_elements(by_locator))} элементов')
        return len(self.find_elements(by_locator))

    def values_is_equal(self, a, b):
        """
        Проверка, что выражение верно

        """
        assert a == b, f'Ожидалось True, получено False сравнивали {a} и {b}'
