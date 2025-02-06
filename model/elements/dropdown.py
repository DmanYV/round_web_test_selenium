from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from base.base_page import BasePage


class Dropdown(BasePage):
    """ Класс, описывающий действия с Drodown на страницах """

    def select_from_dropdown(self, by_locator: tuple[str, str], value: str or int, timeout: int = 10):
        try:
            # Ожидание появления элемента
            element = WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located(locator=by_locator)
            )

            # Создание объекта Select
            select = Select(webelement=element)

            # Определение типа value и выбор соответствующего метода
            if isinstance(value, int) or (isinstance(value, str) and value.isdigit()):
                select.select_by_index(int(value))
            else:
                select.select_by_visible_text(str(value))
        except TimeoutException:
            raise TimeoutException(f'Элемент {by_locator} не появился после {timeout} секунд')
        except Exception as e:
            raise Exception(f'Не удалось выбрать значение {value} из выпадающего списка {by_locator}: {e}')