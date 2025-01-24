import allure
import pytest
import psycopg

from selenium import webdriver
from selenium.common import TimeoutException

import config.locators
from config import attach
from selenium.webdriver.chrome.options import Options
from base.app_locators import *
from model.api.authorization import *
from settings import User, DB


@pytest.fixture(autouse=True, scope='function')
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')  # размер окна is 1920x1080
    chrome_options.add_argument('--no-sandbox')  # no sandbox
    chrome_options.add_argument('--disable-dev-shm-usage')  # overcome limited resource problems
    # chrome_options.add_argument('--incognito')  # режим инкогнито
    chrome_options.add_argument('--headless')  # режим без UI
    # chrome_options.add_argument('--ignore-certificate-errors')  # режим игнорирования сертификата
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver

    attach.add_html(driver)
    attach.add_screenshot(driver)
    attach.add_logs(driver)

    driver.quit()


@pytest.fixture(scope='function')
@allure.title('Инициализация локаторов')
@allure.step('Инициализация локаторов')
def elements(request) -> dict:
    elements = Locators.elements
    request.cls.elements = elements
    return elements


@pytest.fixture(scope='function')
@allure.title('Авторизация пользователя в системе')
@allure.step('Авторизация пользователя в системе')
def login_to_app(request, driver):
    """ Фикстура Логина в систему """
    login_page = ApiAuthorization(driver)
    login_page.user(User.LOGIN, User.PASSWORD)
    try:
        later = login_page.find_element(config.locators.RubricPageLocators.locators['Кнопка выберу потом'])
        login_page.do_click(later)
    except TimeoutException:
        element = login_page.find_element(
            config.locators.MainPageLocators.locators['Листай вниз и найди свои интересы'])
        login_page.do_click(element)


@pytest.fixture(scope="module")
@allure.title('Установка соединения с БД')
@allure.step('Установка соединения с БД')
def db_connection(request):
    """
    Фикстура для установки соединения с базой данных.

    Args:
        request: объект запроса pytest.

    Returns:
        connection: объект соединения с базой данных.

    Raises:
        Exception: если возникает ошибка при подключении к базе данных.
    """
    connection = None
    try:
        connection = psycopg.connect(
            dbname=DB.DBNAME,
            user=DB.DBUSER,
            password=DB.DBPASSWORD,
            host=DB.DBHOST,
            port=DB.DBPORT
        )
        print('Соединение с БД установлено успешно')

        def fin():
            if connection:
                connection.close()
                print('Соединение с БД закрыто')

        request.addfinalizer(fin)
        return connection
    except Exception as error:
        print(f'Ошибка при подключении к БД: {error}')
        if connection:
            connection.close()
            print('Соединение с БД закрыто')
