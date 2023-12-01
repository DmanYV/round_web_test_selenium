import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    """Основной класс страницы от которого наследуем"""
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://staging.round.zone'

    def open(self):
        """Функция открытия страницы"""
        self.driver.get(self.PAGE_URL)

    def is_open(self, wait_time=10):
        """Функция проверка, что запрашиваемая страница открыта"""
        WebDriverWait(self.driver, wait_time).until(EC.url_to_be(self.PAGE_URL))

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

    def do_click(self, locator, wait_time=10):
        """Функция клик на элемент с ожиданием, что элемент кликабелен"""
        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(locator)).click()

    def find_element(self, locator, wait_time=10):
        """Функция поиска элемента с ожиданием, что элемент видим на странице и в DOM"""
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator), message=f'Не найден элемент с локатором {locator}')

    def find_elements(self, locator, wait_time=10):
        """Функция поиска элемента с ожиданием, что элемент видим на странице и в DOM"""
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_all_elements_located(locator), message=f'Не найдены элементы с локатором {locator}')

    def element_is_present(self, locator, wait_time=10):
        """Функция поиска элемента в DOM"""
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator))

    def elements_is_present(self, locator, wait_time=10):
        """Функция поиска элемента в DOM"""
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, wait_time=10):
        """Функция поиска элемента, который не видим и отсутствует в DOMe"""
        return WebDriverWait(self.driver, wait_time).until(EC.invisibility_of_element_located(locator))

    def clear(self, locator, wait_time=10):
        """Функция очистки поля"""
        element = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator))
        element.clear()

    def assert_open_url(self, url):
        """
        Функция проверки URL.
        URL - передаем ожидаемое значение
        """
        assert self.driver.current_url == url, 'Открытая страница не соответствует' + ' ' + url
