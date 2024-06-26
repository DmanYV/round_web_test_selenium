import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.locators import AllPageLocators


class BasePage(object):
    """Основной класс страницы от которого наследуем"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=1.5)
        self.base_url = 'https://staging.round.zone'

    def open(self):
        """Функция открытия страницы"""
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        """Функция проверка, что запрашиваемая страница открыта"""
        self.element_is_not_visible(AllPageLocators.SPINNER)
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def switch_to_tab(self, tab_index: int):
        """Переключение по вкладкам. В tab_index передаем цифру-индекс вкладки"""
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
        """Функция клик на элемент с ожиданием, что элемент кликабелен"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def field_send_keys(self, locator: tuple, text: str) -> None:
        """Функция ввода текста в поле"""
        element = self.find_element(locator)
        element.send_keys(text)

    def find_element(self, locator):
        """Функция поиска элемента с ожиданием, что элемент видим на странице и в DOM"""
        return self.wait.until(EC.visibility_of_element_located(locator),
                               message=f'Не найден элемент с локатором {locator}')

    def find_elements(self, locator):
        """Функция поиска элемента с ожиданием, что элемент видим на странице и в DOM"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator),
                               message=f'Не найдены элементы с локатором {locator}')

    def element_is_present(self, locator):
        """Функция поиска элемента в DOM"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_is_present(self, locator):
        """Функция поиска элемента в DOM"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator):
        """Функция поиска элемента, для проверки его отсутствия в DOMe"""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def clear(self, locator):
        """Функция очистки поля"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
