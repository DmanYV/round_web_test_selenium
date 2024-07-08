import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    """Основной класс страницы от которого наследуем"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=1.5)
        self.base_url = 'https://staging.round.zone'

    def open(self):
        """Функция открытия страницы"""
        self.driver.get(self.PAGE_URL)

    def switch_iframe(self, locator):
        """

        Функция переключения на iframe

        :param locator:
            локатор элемента

        """
        iframe = self.find_element(locator)
        self.driver.switch_to.frame(iframe)

    def switch_to_tab(self, tab_index: int):
        """

        Переключение по вкладкам. В tab_index передаем цифру-индекс вкладки

        :param tab_index:
            цифру-индекс вкладки

        """
        time.sleep(1)
        all_tabs = self.driver.window_handles

        if len(all_tabs) == 1:
            print('Одна вкладка доступна')
            self.driver.switch_to.window(all_tabs[tab_index])
        else:
            self.driver.switch_to.window(all_tabs[tab_index])
            time.sleep(1)

    def close_driver(self):
        """Функция закрытия браузера"""
        self.driver.close()

    def do_click(self, locator):
        """

        Функция клик на элемент с ожиданием, что элемент кликабелен

        :param locator:
            локатор элемента
        """
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def field_send_keys(self, locator: tuple, text: str or int) -> None:
        """

        Функция ввода текста в поле

        :param locator:
            локатор элемента
        :param text:
            текст для ввода

        """
        element = self.find_element(locator)
        element.send_keys(text)

    def find_element(self, locator):
        """

        Функция поиска элемента с ожиданием, что элемент видим на странице и в DOM

        :param locator:
            локатор элемента

        """
        return self.wait.until(EC.visibility_of_element_located(locator),
                               message=f'Не найден элемент с локатором {locator}')

    def find_elements(self, locator):
        """

        Функция поиска элемента с ожиданием, что элемент видим на странице и в DOM

        :param locator:
            локатор элемента

        """
        return self.wait.until(EC.visibility_of_all_elements_located(locator),
                               message=f'Не найдены элементы с локатором {locator}')

    def element_is_present(self, locator):
        """

        Функция поиска элемента в DOM

        :param locator:
            локатор элемента

        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_is_present(self, locator):
        """
        Функция поиска элемента в DOM

        :param locator:
            локатор элемента

        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator):
        """
        Функция поиска элемента, для проверки его отсутствия в DOMe

        :param locator:
            локатор элемента

        """
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def clear(self, locator):
        """
        Функция очистки поля

        :param locator:
            локатор элемента

        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
