import allure
import pytest
from faker import Faker

import config.locators

from model.pages.authorization_page import AuthorizationPage
from model.pages.join_page import JoinPage
from base.base_assertion import Assertion
from model.api.metabase import MetaBase
from model.pages.main_page import MainPage
from model.pages.rubric_page import RubricPage
from settings import User, MetaBaseUser

fake = Faker()


@pytest.fixture(scope='function')
@allure.title('Регистрация пользователя')
@allure.step('Регистрация пользователя')
def registration_user(driver):
    """
    Фикстура регистрации нового пользователя

    :param driver:
        принимает в себя экземпляр драйвера

    """
    authorization_page = AuthorizationPage(driver)
    join_page = JoinPage(driver)
    metabase = MetaBase(driver)
    assertion = Assertion(driver)
    rubric_page = RubricPage(driver)
    main_page = MainPage(driver)

    authorization_page.open()
    authorization_page.do_click(config.locators.AuthorizationPageLocators.locators['Кнопка по смс'])
    join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка далее'])
    username = f'-{fake.pystr(min_chars=5, max_chars=11)}.{fake.pyint(min_value=1, max_value=2)}_'
    join_page.field_send_keys(config.locators.JoinPageLocators.locators['Поле никнейм'], text=f'{username}')
    join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка далее'])
    join_page.field_send_keys(config.locators.JoinPageLocators.locators['Поле пароль'], text=User.PASSWORD)
    join_page.field_send_keys(config.locators.JoinPageLocators.locators['Поле повтори пароль'], text=User.PASSWORD)
    join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка далее'])
    phone_number = fake.random_number(digits=10, fix_len=True)
    join_page.field_send_keys(config.locators.JoinPageLocators.locators['Поле номер телефона'], text=phone_number)
    join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка далее'])
    cooke = metabase.authorization(username=MetaBaseUser.LOGIN,
                                   password=MetaBaseUser.PASSWORD)
    sms_code = metabase.take_last_code(cooke)
    join_page.field_send_keys(config.locators.JoinPageLocators.locators['Поле проверочный код'], text=sms_code)
    assertion.text_in_element(config.locators.JoinPageLocators.locators['Текст приветствия пользователя'],
                              expected_text=f'Привет, {username[:16]}\nДобро пожаловать в Round!')
    join_page.do_click(config.locators.JoinPageLocators.locators['Кнопка погнали'])
    element = rubric_page.find_element(config.locators.RubricPageLocators.locators['Кнопка выберу потом'])
    rubric_page.do_click(element)
    element = main_page.find_element(config.locators.MainPageLocators.locators['Листай вниз и найди свои интересы'])
    main_page.do_click(element)
