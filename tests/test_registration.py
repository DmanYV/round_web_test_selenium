import time

import allure
import pytest
from faker import Faker

from base.base_test import BaseTest

fake = Faker()
fakeru = Faker("ru_RU")


@allure.feature('Регистрация пользователя')
@pytest.mark.registration
class TestRegistrationUser(BaseTest):
    @allure.title('Регистрация пользователя по номеру телефона')
    @allure.description('При проверке так же проверяем, что никнейм может иметь в себе: '
                        'цифры, точку (только в середине), дефис, нижнее подчеркивание')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_registering_a_new_user_by_phone_number(self, elements, db_connection):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.user_name()}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            self.join_page.field_send_keys(element['Поле пароль'], text=self.User.PASSWORD)

        with allure.step('В поле Повтори пароль ввести пароль еще раз'):
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=self.User.PASSWORD)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Ввести номер телефона в поле номер телефона'):
            phone_number = fakeru.random_number(digits=10, fix_len=True)
            self.join_page.field_send_keys(element['Поле номер телефона'], text=phone_number)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Подключиться к базе данных и получить смс код'):
            sms_code = self.db_round_confirmation.get_last_sms_code(db_connection)

        with allure.step('Ввести смс код'):
            self.login_page.field_send_keys(element['Поле проверочный код'], text=sms_code)

        with allure.step('Проверить, что пользователю отображается окно приветствия'):
            self.assertion.text_in_element(element['Текст приветствия пользователя'],
                                           expected_text=f'Привет, {username[:16]}\nДобро пожаловать в Round!')

    @allure.title('Проверка возможности выбора возраста пользователя')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_checking_the_user_age_choice_during_registration(self, elements):
        with allure.step('Открыть страницу регистрации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать на выпадающий список с датами рождения'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Поле год рождения'])
        with allure.step('В выпадающем списке выбрать поочередно с 2014 по 2010 год'):
            self.join_page.do_click(element['2014 год'])
            self.join_page.do_click(element['Поле год рождения'])
            self.join_page.do_click(element['2013 год'])
            self.join_page.do_click(element['Поле год рождения'])
            self.join_page.do_click(element['2012 год'])
        with allure.step('Проверить, что в поле теперь отображается 2012 год'):
            self.assertion.text_in_element(element['Поле год рождения'], expected_text='2012')

    @allure.title('Проверка валидации поля никнейм при вводе менее 3 символов')
    @allure.severity('Normal')
    @pytest.mark.regression
    def test_validation_of_the_nickname_field_when_entering_less_than_3_characters(self, elements):
        with allure.step('Открыть страницу регистрации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести менее 3 символов'):
            self.join_page.field_send_keys(element['Поле никнейм'], text=fake.pystr(min_chars=1, max_chars=2))

        with allure.step('Проверить, что отображается валидация поля никнейм: '
                         '"- длина от 3 до 16 символов;'
                         ' - только английские буквы;'
                         ' - можно цифры;'
                         ' - можно точку (только в середине), дефис, нижнее подчеркивание;'
                         ' - нельзя использовать пробелы."'):
            self.assertion.text_in_element(element['Валидация поля никнейм'],
                                           expected_text='- длина от 3 до 16 символов;\n\n'
                                                         '- только английские буквы;\n\n'
                                                         '- можно цифры;\n\n'
                                                         '- можно точку (только в середине), дефис, нижнее подчеркивание;\n\n'
                                                         '- нельзя использовать пробелы.')

    @allure.title('Проверка валидации поля никнейм при вводе более 16 символов')
    @allure.severity('Normal')
    @pytest.mark.regression
    def test_validation_field_nickname_when_entering_more_than_16_characters(self, elements):
        with allure.step('Открыть страницу регистрации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести 16 символов'):
            self.join_page.field_send_keys(element['Поле никнейм'], text=fake.pystr(min_chars=16))

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Проверить, что в поле видимо поле ввода пароля и повторения пароля'):
            self.assertion.is_elem_displayed(element['Поле пароль'])
            self.assertion.is_elem_displayed(element['Поле повтори пароль'])

    @allure.title('Проверка валидации поля никнейм при вводе русских символов')
    @allure.severity('Normal')
    @pytest.mark.regression
    def test_validation_field_nickname_when_entering_russian_characters(self, elements):
        with allure.step('Открыть страницу регистрации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести от 3 до 16 символов на русском языке'):
            self.join_page.field_send_keys(element['Поле никнейм'], text=fakeru.first_name())

        with allure.step('Проверить, что отображается валидация поля никнейм: '
                         '"- длина от 3 до 16 символов;'
                         ' - только английские буквы;'
                         ' - можно цифры;'
                         ' - можно точку (только в середине), дефис, нижнее подчеркивание;'
                         ' - нельзя использовать пробелы."'):
            self.assertion.text_in_element(element['Валидация поля никнейм'],
                                           expected_text='- длина от 3 до 16 символов;\n\n'
                                                         '- только английские буквы;\n\n'
                                                         '- можно цифры;\n\n'
                                                         '- можно точку (только в середине), дефис, нижнее подчеркивание;\n\n'
                                                         '- нельзя использовать пробелы.')

    @allure.title('Проверка валидации поля никнейм при вводе пробела')
    @allure.severity('Normal')
    @pytest.mark.regression
    def test_validation_field_nickname_when_entering_a_space(self, elements):
        with allure.step('Открыть страницу регистрации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести от 3 до 15 символов и в конце пробел'):
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{fakeru.pystr(min_chars=3, max_chars=15)} ')

        with allure.step('Проверить, что отображается валидация поля никнейм: '
                         '"- длина от 3 до 16 символов;'
                         ' - только английские буквы;'
                         ' - можно цифры;'
                         ' - можно точку (только в середине), дефис, нижнее подчеркивание;'
                         ' - нельзя использовать пробелы."'):
            self.assertion.text_in_element(element['Валидация поля никнейм'],
                                           expected_text='- длина от 3 до 16 символов;\n\n'
                                                         '- только английские буквы;\n\n'
                                                         '- можно цифры;\n\n'
                                                         '- можно точку (только в середине), дефис, нижнее подчеркивание;\n\n'
                                                         '- нельзя использовать пробелы.')

    @allure.title('Проверка валидации поля никнейм при вводе уже зарегистрированного никнейма')
    @allure.severity('Normal')
    @pytest.mark.regression
    def test_validation_field_nickname_when_entering_an_already_registered_nickname(self, elements):
        with allure.step('Открыть страницу регистрации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести Aleska'):
            self.join_page.field_send_keys(element['Поле никнейм'], text='Aleska')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Проверить, что отображается валидация поля никнейм: Данный Никнейм уже занят'):
            self.assertion.text_in_element(element['Валидация поля никнейм'], expected_text='Данный Никнейм уже занят')

    @allure.title('Проверка получения СМС с кодом подтверждения регистрации')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_receiving_sms_with_registration_confirmation_code(self, elements, db_connection):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.user_name()}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            self.join_page.field_send_keys(element['Поле пароль'], text=self.User.PASSWORD)

        with allure.step('В поле Повтори пароль ввести пароль еще раз'):
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=self.User.PASSWORD)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Ввести номер телефона в поле номер телефона'):
            phone_number = fakeru.random_number(digits=10, fix_len=True)
            self.join_page.field_send_keys(element['Поле номер телефона'], text=phone_number)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Получаем смс код из Базы данных'):
            sms_code = self.db_round_confirmation.get_last_sms_code(db_connection)

        with allure.step('Проверяем, что код пришел'):
            assert sms_code.isdigit()

    @allure.title('Проверка возможности повторно запросить код')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_possibility_to_re_request_code(self, elements, db_connection):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.user_name()}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            self.join_page.field_send_keys(element['Поле пароль'], text=self.User.PASSWORD)

        with allure.step('В поле Повтори пароль ввести пароль еще раз'):
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=self.User.PASSWORD)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Ввести номер телефона в поле номер телефона'):
            phone_number = fakeru.random_number(digits=10, fix_len=True)
            self.join_page.field_send_keys(element['Поле номер телефона'], text=phone_number)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Получаем первый смс код из Базы данных'):
            first_sms_code = self.db_round_confirmation.get_last_sms_code(db_connection)

        with allure.step('Подождать 1 минуту, пока закончится таймер'):
            time.sleep(65)

        with allure.step('Проверить, что кнопка "Запросить код еще раз появилась"'):
            self.assertion.is_elem_displayed(element['Кнопка запросить код еще раз'])

        with allure.step('Нажать кнопку "Запросить код еще раз появилась"'):
            self.join_page.do_click(element['Кнопка запросить код еще раз'])

        with allure.step('Проверяем что пришел новый смс код'):
            last_sms_code = self.db_round_confirmation.get_last_sms_code(db_connection)
            assert first_sms_code != last_sms_code

    @allure.title('Проверка валидации поля смс кода на ввод неверного значения')
    @allure.description('В поле вводится рандомный текст или код')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_to_validate_the_sms_code_field_for_entering_an_incorrect_value(self, elements):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.user_name()}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            self.join_page.field_send_keys(element['Поле пароль'], text=self.User.PASSWORD)

        with allure.step('В поле Повтори пароль ввести пароль еще раз'):
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=self.User.PASSWORD)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Ввести номер телефона в поле номер телефона'):
            phone_number = fakeru.random_number(digits=10, fix_len=True)
            self.join_page.field_send_keys(element['Поле номер телефона'], text=phone_number)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Ввести в поле смс код случайный текст или номер'):
            self.login_page.field_send_keys(element['Поле проверочный код'],
                                            text=f'{fake.pyint(min_value=1000, max_value=9999)}')

        with allure.step('Проверить, что сработала валидация с текстом "Код введен неверно"'):
            self.assertion.text_in_element(element['Валидация поля проверочный код'],
                                           expected_text='Код введен неверно')

    @allure.title('Проверка валидации поля "Номер телефона" при вводе уже зарегистрированного номера')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_validation_of_the_phone_number_field_when_entering_an_already_registered_number(self, elements):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.pystr(min_chars=5, max_chars=11)}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            self.join_page.field_send_keys(element['Поле пароль'], text=self.User.PASSWORD)

        with allure.step('В поле Повтори пароль ввести пароль еще раз'):
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=self.User.PASSWORD)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Ввести номер телефона в поле номер телефона'):
            self.join_page.field_send_keys(element['Поле номер телефона'], text=self.User.PHONE[1:])

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Проверить, что отображается валидация поля с текстом "Телефон уже используется"'):
            self.assertion.text_in_element(element['Валидация поля номер телефона'],
                                           expected_text='Телефон уже используется')

    @allure.title('Проверка валидации поля "Номер телефона" при вводе менее 10 цифр')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_validation_of_the_phone_number_field_when_entering_less_than_10_digits(self, elements):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.user_name()}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            self.join_page.field_send_keys(element['Поле пароль'], text=self.User.PASSWORD)

        with allure.step('В поле Повтори пароль ввести пароль еще раз'):
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=self.User.PASSWORD)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Ввести номер телефона в поле номер телефона'):
            phone_number = fakeru.random_number(digits=9, fix_len=False)
            self.join_page.field_send_keys(element['Поле номер телефона'], text=phone_number)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step(
                'Проверить, что отображается валидация поля с текстом: "Проверь правильность телефонного номера"'):
            self.assertion.text_in_element(element['Валидация поля номер телефона'],
                                           expected_text='Проверь правильность телефонного номера')

    @allure.title('Проверка валидации поля "Пароль" при вводе пароля от 6 букв')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_validation_of_the_password_field_when_entering_a_password_of_6_letters_or_more(self, elements):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.user_name()}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            password = fake.pystr(min_chars=6, max_chars=128)
            self.join_page.field_send_keys(element['Поле пароль'], text=password)

        with allure.step('В поле Повтори пароль ввести пароль еще раз'):
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=password)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Проверить, что под полем "Пароль" отображается валидация с текстом:'
                         ' "Использование цифр обязательно. Принимаются пароли от 6 символов английской раскладки"'):
            self.assertion.text_in_element(element['Валидация поля пароль'],
                                           expected_text='Использование цифр обязательно. '
                                                         'Принимаются пароли от 6 символов английской раскладки')

    @allure.title('Проверка валидации поля "Пароль" при вводе пароля от 6 цифр')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_validation_of_the_password_field_when_entering_a_password_of_6_digit_or_more(self, elements):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.user_name()}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            password = fake.pyint(min_value=100000, max_value=128000000)
            self.join_page.field_send_keys(element['Поле пароль'], text=password)

        with allure.step('В поле Повтори пароль ввести пароль еще раз'):
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=password)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Проверить, что под полем "Пароль" отображается валидация с текстом:'
                         ' "Обязательно используй буквы английской раскладки (от 6 символов, включая цифры)"'):
            self.assertion.text_in_element(element['Валидация поля пароль'],
                                           expected_text='Обязательно используй буквы английской раскладки '
                                                         '(от 6 символов, включая цифры)')

    @allure.title('Проверка валидации поля "Повтори пароль" при вводе разных паролей')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_validation_of_the_repeat_password_field_when_entering_different_passwords(self, elements):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.user_name()}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            self.join_page.field_send_keys(element['Поле пароль'], text=self.User.PASSWORD)

        with allure.step('В поле Повтори пароль ввести пароль не совпадающий с полем Пароль'):
            password = fake.pyint(min_value=100000, max_value=128000000)
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=password)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Проверить, что под полем "Пароль" отображается валидация с текстом: Пароли не совпадают.'):
            self.assertion.text_in_element(element['Валидация поля повтори пароль'],
                                           expected_text='Пароли не совпадают.')

    @allure.title('Проверка валидации поля "Код приглашения" при вводе случайного значения')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_validation_of_the_invitation_code_field_when_entering_a_random_value(self, elements):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.user_name()}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            self.join_page.field_send_keys(element['Поле пароль'], text=self.User.PASSWORD)

        with allure.step('В поле Повтори пароль ввести пароль еще раз'):
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=self.User.PASSWORD)

        with allure.step('Нажать на чекбокс "У меня есть код приглашения"'):
            self.join_page.do_click(element['Чекбокс код приглашения'])

        with allure.step('В поле код приглашения ввести рандомный текст'):
            self.join_page.field_send_keys(element['Поле код приглашения'], text=fake.pystr())

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Проверить, что под полем "Код приглашения" сработала валидация с текстом:'
                         ' "Неверный код приглашения"'):
            self.assertion.text_in_element(element['Валидация поля код приглашения'],
                                           expected_text='Неверный код приглашения')

    @allure.title('Проверка валидации поля "Код приглашения" при вводе валидного значения')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_validation_of_the_invitation_code_field_when_entering_an_invalid_value(self, elements):
        with allure.step('Открыть страницу авторизации'):
            self.authorization_page.open()
            element = elements['Страница авторизации']

        with allure.step('Нажать кнопку "По смс (Для России)"'):
            self.authorization_page.do_click(element['Кнопка по смс'])

        with allure.step('Нажать кнопку Далее'):
            element = elements['Страница регистрации']
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле никнейм ввести любое валидное значение'):
            username = f'-{fake.user_name()}.{fake.pyint(min_value=1, max_value=2)}_'
            self.join_page.field_send_keys(element['Поле никнейм'], text=f'{username}')

        with allure.step('Нажать кнопку Далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('В поле Пароль ввести пароль'):
            self.join_page.field_send_keys(element['Поле пароль'], text=self.User.PASSWORD)

        with allure.step('В поле Повтори пароль ввести пароль еще раз'):
            self.join_page.field_send_keys(element['Поле повтори пароль'], text=self.User.PASSWORD)

        with allure.step('Нажать на чекбокс "У меня есть код приглашения"'):
            self.join_page.do_click(element['Чекбокс код приглашения'])

        with allure.step('В поле код приглашения ввести рандомный текст'):
            self.join_page.field_send_keys(element['Поле код приглашения'], text=self.User.INVCODE)

        with allure.step('Нажать кнопку далее'):
            self.join_page.do_click(element['Кнопка далее'])

        with allure.step('Проверить, что на экране видно поле ввода номера телефона'):
            self.assertion.is_elem_displayed(element['Поле номер телефона'])
