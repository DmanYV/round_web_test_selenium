import allure
import pytest
from faker import Faker

from base.base_test import BaseTest

fake = Faker()
fakeru = Faker("ru_RU")


@allure.feature('Восстановление пароля')
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

    @allure.title('Проверка восстановления пароля по номеру телефона')
    @allure.description('Для восстановления используется номер от Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_password_recovery_by_phone(self, elements):
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

        with allure.step('Авторизоваться в MetaBase'):
            metabase = self.metabase.authorization(username=self.MetaBaseUser.LOGIN,
                                                   password=self.MetaBaseUser.PASSWORD)

        with allure.step('Найти последний код в MetaBase'):
            sms_code = self.metabase.take_last_code(metabase)

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

        with allure.step('Проверить что открыта страница рубрики'):
            self.assertion.page_is_opened(page_url=self.rubric_page.PAGE_URL)

    @allure.title('Проверка получения смс кода для сброса пароля')
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

        with allure.step('Авторизоваться в MetaBase'):
            metabase = self.metabase.authorization(username=self.MetaBaseUser.LOGIN,
                                                   password=self.MetaBaseUser.PASSWORD)

        with allure.step('Найти последний код в MetaBase и проверить, что он пришел'):
            sms_code = self.metabase.take_last_code(metabase)
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

        with allure.step('Проверить, что сработала валидация с текстом "Код введен неверно"'):
            self.assertion.text_in_element(element['Валидация поля код из смс'],
                                           expected_text='Код введен неверно')

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

        with allure.step('Проверить, что сработала валидация с текстом "Пользователь не найден"'):
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

        with allure.step('Проверить, что сработала валидация с текстом "Пользователь не найден"'):
            self.assertion.text_in_element(element['Валидация поля логин'],
                                           expected_text='Пользователь не найден')
