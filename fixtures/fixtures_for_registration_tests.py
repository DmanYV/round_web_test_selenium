import allure
import pytest
from faker import Faker
from selenium.common import TimeoutException

import config.locators

from model.pages.authorization_page import AuthorizationPage
from model.pages.join_page import JoinPage
from base.base_assertion import Assertion
from model.sql.db_round_confirmation import DBRoundConfirmation
from model.pages.main_page import MainPage
from model.pages.rubric_page import RubricPage
from settings import User

fake = Faker()


@pytest.fixture(scope='function')
@allure.title('Регистрация пользователя')
@allure.step('Регистрация пользователя')
def registration_user(driver, db_connection):
    """
    Фикстура для регистрации нового пользователя в системе.

    Эта фикстура выполняет полный процесс регистрации нового пользователя,
    включая заполнение всех необходимых полей и прохождение верификации по SMS.

    Процесс регистрации:
    1. Открывает страницу авторизации
    2. Выбирает регистрацию по SMS
    3. Генерирует случайный никнейм
    4. Вводит пароль
    5. Генерирует случайный номер телефона
    6. Получает код подтверждения из Database
    7. Вводит код подтверждения
    8. Проверяет приветственное сообщение
    9. Закрывает приветственное видео (если оно есть)
    10. Пропускает выбор рубрик
    11. Закрывает окно с предложением листать ленту

    :param driver: экземпляр WebDriver для управления браузером
    :param db_connection: экземпляр подключения к базе данных ROUND

    :return: None

    Примечание:
    - Использует faker для генерации случайных данных
    - Взаимодействует с MetaBase для получения кода подтверждения
    - Обрабатывает возможные исключения, такие как отсутствие приветственного видео
    """
    authorization_page = AuthorizationPage(driver)
    join_page = JoinPage(driver)
    db = DBRoundConfirmation(driver)
    assertion = Assertion(driver)
    rubric_page = RubricPage(driver)
    main_page = MainPage(driver)

    # Открываем страницу авторизации и выбираем регистрацию по SMS
    authorization_page.open()
    authorization_page.do_click(config.locators.AuthorizationPageLocators.locators['Кнопка по смс'])
    join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка далее'])

    # Генерируем случайный никнейм и вводим его
    username = f'-{fake.pystr(min_chars=5, max_chars=11)}.{fake.pyint(min_value=1, max_value=2)}_'
    join_page.field_send_keys(config.locators.JoinPageLocators.locators['Поле никнейм'], text=f'{username}')
    join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка далее'])

    # Вводим пароль и подтверждаем его
    join_page.field_send_keys(config.locators.JoinPageLocators.locators['Поле пароль'], text=User.PASSWORD)
    join_page.field_send_keys(config.locators.JoinPageLocators.locators['Поле повтори пароль'], text=User.PASSWORD)
    join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка далее'])

    # Генерируем случайный номер телефона и вводим его
    phone_number = fake.random_number(digits=10, fix_len=True)
    join_page.field_send_keys(config.locators.JoinPageLocators.locators['Поле номер телефона'], text=phone_number)
    join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка далее'])

    # Получаем код подтверждения из MetaBase и вводим его
    sms_code = db.get_last_sms_code(connection=db_connection)
    join_page.field_send_keys(config.locators.JoinPageLocators.locators['Поле проверочный код'], text=sms_code)

    # Проверяем приветственное сообщение и нажимаем кнопку "Погнали"
    assertion.text_in_element(config.locators.JoinPageLocators.locators['Текст приветствия пользователя'],
                              expected_text=f'Привет, {username[:16]}\nДобро пожаловать в Round!')
    join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка погнали'])

    # Закрываем приветственное видео (если оно есть)
    try:
        join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка закрыть видео'])
    except TimeoutException:
        pass

    # Пропускаем выбор рубрик и закрываем окно с предложением листать ленту
    element = rubric_page.find_element(config.locators.RubricPageLocators.locators['Кнопка выберу потом'])
    rubric_page.do_click(element)
    element = main_page.find_element(config.locators.MainPageLocators.locators['Листай вниз и найди свои интересы'])
    main_page.do_click(element)
