import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from config.locators import AllPageLocators


class Assertion(BasePage):
    def text_in_element(self, by_locator, expected_text: str or int, timeout=10):
        """
        Проверка совпадения текста элемента с ожиданием

        :param by_locator:
            локатор элемента
        :param expected_text:
            ожидаемый текст
        :param timeout:
            время ожидания в секундах

        """

        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(by_locator)
        )

        text_in_element = element.text
        assert expected_text == text_in_element, \
            f"Ожидался текст: '{expected_text}', отображается текст: '{text_in_element}'"

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

    def page_is_opened(self, page_url, timeout=10):
        """
        Функция проверки, что запрашиваемая страница открыта

        :param page_url:
            url страницы
        :param timeout:
            время ожидания в секундах
        """
        try:
            self.element_is_not_visible(AllPageLocators.locators['Спиннер загрузки'])
            self.wait.until(EC.url_to_be(page_url), timeout)
        except TimeoutException:
            current_url = self.driver.current_url
            raise AssertionError(f'Ожидалась страница {page_url}, но открылась {current_url}. '
                                 f'Страница не загрузилась за {timeout} секунд.')

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

    @staticmethod
    def values_is_equal(a, b):
        """
        Проверка, что выражение верно

        :param a:
            первое значение
        :param b:
            второе значение

        """
        assert a == b, f'Ожидалось True, получено False сравнивали {a} и {b}'

    def checkbox_status(self, by_locator: tuple):
        """
        Определяет простановку чекбокса

        :param by_locator:
            Локатор чекбокса
        """

        checkbox = self.driver.find_element(by_locator)

        assert checkbox.is_selected()
