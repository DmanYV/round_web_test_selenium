import time

import allure
import pytest
from faker import Faker

from base.base_test import BaseTest

fake = Faker()
fakeru = Faker("ru_RU")


@allure.feature('Восстановление пароля')
@pytest.mark.reset_password
class TestResetPassword(BaseTest):
    @allure.title('Проверка нажатия кнопки "Забыл(-а) пароль?"')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_button_press_forgot_password(self, elements):
        with allure.step('Открыть страницу авторизации'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('Нажать кнопку "Забыл(-а) пароль?"'):
            self.authorization_page.do_click(element['Кнопка забыл пароль'])

        with allure.step('Проверить, что открыта страница Восстановления пароля'):
            self.assertion.page_is_opened(page_url=self.reset_password_page.PAGE_URL)

    @allure.id(25)
    @allure.link('https://team-n5un.testit.software/projects/1/tests/25')
    @allure.title('Проверка восстановления пароля по номеру телефона')
    @allure.description('Для восстановления используется номер от Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_password_recovery_by_phone(self, elements, db_connection):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('Нажать кнопку забыл пароль'):
            self.login_page.do_click(element['Кнопка забыл пароль'])

        with allure.step('В поле "Email или номер телефона" ввести номер телефона от Aleska'):
            element = elements['Страница восстановления пароля']
            self.reset_password_page.field_send_keys(element['Поле логин'],
                                                     text=self.User.PHONE)

        with allure.step('Нажать кнопку "Сбросить пароль"'):
            self.reset_password_page.do_click(element['Кнопка сбросить пароль'])

        with allure.step('Получить смс код из Базы данных'):
            sms_code = self.db_round_confirmation.get_last_sms_code(db_connection)

        with allure.step('В поле Код из смс ввести смс код'):
            self.reset_password_page.field_send_keys(element['Поле код из смс'],
                                                     text=sms_code)

        with allure.step('В поле пароль ввести новый пароль'):
            self.reset_password_page.field_send_keys(element['Поле пароль'],
                                                     text=self.User.PASSWORD)

        with allure.step('В поле повтори пароль ввести новый пароль'):
            self.reset_password_page.field_send_keys(element['Поле повтори пароль'],
                                                     text=self.User.PASSWORD)

        with allure.step('Нажать кнопку сохранить'):
            self.reset_password_page.do_click(element['Кнопка сохранить'])

        with allure.step('Проверить, что отображается окно с текстом "Пароль изменен"'):
            self.assertion.text_in_element(element['Диалоговое окно пароль изменен'],
                                           expected_text='Пароль изменен')

        with allure.step('Нажать кнопку "Хорошо"'):
            self.reset_password_page.do_click(element['Кнопка хорошо'])

        with allure.step('Проверить что открыта главная страница'):
            self.assertion.page_is_opened(page_url=self.main_page.PAGE_URL)

    @allure.id(26)
    @allure.link('https://team-n5un.testit.software/projects/1/tests/26')
    @allure.title('Проверка получения смс кода для сброса пароля')
    @allure.description('Для восстановления используется номер от Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_receiving_sms_code_to_reset_password(self, elements, db_connection):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('Нажать кнопку забыл пароль'):
            self.login_page.do_click(element['Кнопка забыл пароль'])

        with allure.step('В поле "Email или номер телефона" ввести номер телефона от Aleska'):
            element = elements['Страница восстановления пароля']
            self.reset_password_page.field_send_keys(element['Поле логин'],
                                                     text=self.User.PHONE)

        with allure.step('Нажать кнопку "Сбросить пароль"'):
            self.reset_password_page.do_click(element['Кнопка сбросить пароль'])


        with allure.step('Получить смс код из Базы данных'):
            sms_code = self.db_round_confirmation.get_last_sms_code(db_connection)
            assert sms_code.isdigit()

    @allure.title('Проверка валидации поля ввода кода из смс при вводе неверного значения')
    @allure.description('Для восстановления используется номер от Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_receiving_sms_code_to_reset_password(self, elements):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('Нажать кнопку забыл пароль'):
            self.login_page.do_click(element['Кнопка забыл пароль'])

        with allure.step('В поле "Email или номер телефона" ввести номер телефона от Aleska'):
            element = elements['Страница восстановления пароля']
            self.reset_password_page.field_send_keys(element['Поле логин'],
                                                     text=self.User.PHONE)

        with allure.step('Нажать кнопку "Сбросить пароль"'):
            self.reset_password_page.do_click(element['Кнопка сбросить пароль'])

        with allure.step('В поле Код из смс ввести смс код'):
            self.reset_password_page.field_send_keys(element['Поле код из смс'],
                                                     text=f'{fake.pyint(min_value=1000, max_value=9999)}')

        with allure.step('Проверить, что сработала валидация с текстом "Неверный код подтверждения"'):
            self.assertion.text_in_element(element['Валидация поля код из смс'],
                                           expected_text='Неверный код подтверждения')

    @allure.title('Проверка валидации поля ввода Email или номер телефона при вводе несуществующего значения email')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_validation_of_the_email_or_phone_number_input_field_when_entering_a_non_existent_value_email(self, elements):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('Нажать кнопку забыл пароль'):
            self.login_page.do_click(element['Кнопка забыл пароль'])

        with allure.step('В поле "Email или номер телефона" ввести случайное значение email'):
            element = elements['Страница восстановления пароля']
            self.reset_password_page.field_send_keys(element['Поле логин'],
                                                     text=f'{fake.email()}')

        with allure.step('Нажать кнопку "Сбросить пароль"'):
            self.reset_password_page.do_click(element['Кнопка сбросить пароль'])

        with allure.step('Проверить, что отобразилась валидация поля'):
            self.assertion.is_elem_displayed(element['Валидация поля логин'])

        with allure.step('Проверить текст валидации поля "Пользователь не найден"'):
            self.assertion.text_in_element(element['Валидация поля логин'],
                                           expected_text='Пользователь не найден')

    @allure.title('Проверка валидации поля ввода Email или номер телефона при вводе несуществующего значения телефона')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_validation_of_the_email_or_phone_number_input_field_when_entering_a_non_existent_value_phone(self, elements):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('Нажать кнопку забыл пароль'):
            self.login_page.do_click(element['Кнопка забыл пароль'])

        with allure.step('В поле "Email или номер телефона" ввести случайный номер телефона'):
            element = elements['Страница восстановления пароля']
            self.reset_password_page.field_send_keys(element['Поле логин'],
                                                     text=f'{fake.pyint(min_value=70000000000, max_value=79999999999)}')

        with allure.step('Нажать кнопку "Сбросить пароль"'):
            self.reset_password_page.do_click(element['Кнопка сбросить пароль'])

        with allure.step('Проверить, что отобразилась валидация поля'):
            self.assertion.is_elem_displayed(element['Валидация поля логин'])

        with allure.step('Проверить, что сработала валидация с текстом "Пользователь не найден"'):
            self.assertion.text_in_element(element['Валидация поля логин'],
                                           expected_text='Пользователь не найден')

    @allure.title('Проверка восстановления пароля через email')
    @allure.description('Для восстановления используется email от Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_password_recovery_by_email(self, elements, db_connection):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('Нажать кнопку забыл пароль'):
            self.login_page.do_click(element['Кнопка забыл пароль'])

        with allure.step('В поле "Email или номер телефона" ввести номер телефона от Aleska'):
            element = elements['Страница восстановления пароля']
            self.reset_password_page.field_send_keys(element['Поле логин'],
                                                     text=self.User.EMAIL)

        with allure.step('Нажать кнопку "Сбросить пароль"'):
            self.reset_password_page.do_click(element['Кнопка сбросить пароль'])


        with allure.step('Получить email код из Базы данных'):
            email_code = self.db_round_confirmation.get_last_sms_code(db_connection)

        with allure.step('В поле Код из письма ввести код из письма'):
            self.reset_password_page.field_send_keys(element['Поле код из письма'],
                                                     text=email_code)

        with allure.step('В поле пароль ввести новый пароль'):
            self.reset_password_page.field_send_keys(element['Поле пароль'],
                                                     text=self.User.PASSWORD)

        with allure.step('В поле повтори пароль ввести новый пароль'):
            self.reset_password_page.field_send_keys(element['Поле повтори пароль'],
                                                     text=self.User.PASSWORD)

        with allure.step('Нажать кнопку сохранить'):
            self.reset_password_page.do_click(element['Кнопка сохранить'])

        with allure.step('Проверить, что отображается окно с текстом "Пароль изменен"'):
            self.assertion.text_in_element(element['Диалоговое окно пароль изменен'],
                                           expected_text='Пароль изменен')

        with allure.step('Нажать кнопку "Хорошо"'):
            self.reset_password_page.do_click(element['Кнопка хорошо'])

        with allure.step('Проверить что открыта главная страница'):
            self.assertion.page_is_opened(page_url=self.main_page.PAGE_URL)

    @allure.id(22)
    @allure.link('https://team-n5un.testit.software/projects/1/tests/22')
    @allure.title('Генерация кода для восстановления пароля по email')
    @allure.description('Для восстановления используется email от Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_receiving_email_code_to_reset_password(self, elements, db_connection):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('Нажать кнопку забыл пароль'):
            self.login_page.do_click(element['Кнопка забыл пароль'])

        with allure.step('В поле "Email или номер телефона" ввести email от Aleska'):
            element = elements['Страница восстановления пароля']
            self.reset_password_page.field_send_keys(element['Поле логин'],
                                                     text=self.User.EMAIL)

        with allure.step('Нажать кнопку "Сбросить пароль"'):
            self.reset_password_page.do_click(element['Кнопка сбросить пароль'])

        with allure.step('Получить смс код из Базы данных'):
            email_code = self.db_round_confirmation.get_last_sms_code(db_connection)
            assert email_code.isdigit()

    @allure.id(23)
    @allure.link('https://team-n5un.testit.software/projects/1/tests/23')
    @allure.title('Возможность повторно запросить код для подтверждения при постановлении пароля по email')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_opportunity_to_re_request_email_code(self, elements, db_connection):
        with allure.step('Открыть страницу логина'):
            self.login_page.open()
            element = elements['Страница логина']

        with allure.step('Нажать кнопку забыл пароль'):
            self.login_page.do_click(element['Кнопка забыл пароль'])

        with allure.step('В поле "Email или номер телефона" ввести email от Aleska'):
            element = elements['Страница восстановления пароля']
            self.reset_password_page.field_send_keys(element['Поле логин'],
                                                     text=self.User.EMAIL)

        with allure.step('Нажать кнопку "Сбросить пароль"'):
            self.reset_password_page.do_click(element['Кнопка сбросить пароль'])

        with allure.step('Получить смс код из Базы данных'):
            first_email_code = self.db_round_confirmation.get_last_sms_code(db_connection)

        with allure.step('Подождать 1 минуту, пока закончится таймер'):
            time.sleep(65)

        with allure.step('После окончания таймера появилась кнопка “Запросить код еще раз”'):
            self.assertion.is_elem_displayed(element['Кнопка запросить код еще раз'])

        with allure.step('Нажать кнопку "Запросить код еще раз появилась"'):
            self.join_page.do_click(element['Кнопка запросить код еще раз'])

        with allure.step('Кнопка нажимается в БД появляется новый сгенерированный код'):
            last_email_code = self.db_round_confirmation.get_last_sms_code(db_connection)
            assert first_email_code != last_email_code
