import allure
import pytest
from faker import Faker

from base.base_test import BaseTest

fake = Faker()
fakeru = Faker('ru_RU')


@allure.feature('Регистрация пользователя')
class TestRegistrationUser(BaseTest):
    @allure.title('Регистрация пользователя по номеру телефона')
    @allure.description('При проверке так же проверяем, что никнейм может иметь в себе: '
                        'цифры, точку (только в середине), дефис, нижнее подчеркивание')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_registering_a_new_user_by_phone_number(self, elements):
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

        with allure.step('Найти последний код в MetaBase'):
            metabase = self.metabase.authorization(username=self.MetaBaseUser.LOGIN,
                                                   password=self.MetaBaseUser.PASSWORD)
            sms_code = self.metabase.take_last_code(metabase)

        with allure.step('Ввести смс код'):
            self.login_page.field_send_keys(element['Поле проверочный код'], text=sms_code)

        with allure.step('Проверить, что пользователю отображается окно приветствия'):
            self.assertion.text_in_element(element['Текст приветствия пользователя'],
                                           expected_text=f'Привет, {username}\nДобро пожаловать в Round!')

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
            self.join_page.do_click(element['Поле годов рождения'])
        with allure.step('В выпадающем списке выбрать поочередно с 2014 по 2010 год'):
            self.join_page.do_click(element['2014 год'])
            self.join_page.do_click(element['Поле годов рождения'])
            self.join_page.do_click(element['2013 год'])
            self.join_page.do_click(element['Поле годов рождения'])
            self.join_page.do_click(element['2012 год'])
            self.join_page.do_click(element['Поле годов рождения'])
            self.join_page.do_click(element['2011 год'])
            self.join_page.do_click(element['Поле годов рождения'])
            self.join_page.do_click(element['2010 год'])
        with allure.step('Проверить, что в поле теперь отображается 2010 год'):
            self.assertion.text_in_element(element['Поле годов рождения'], expected_text='2010')

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
            self.join_page.field_send_keys(element['Поле никнейм'], text=fake.pystr(min_chars=0, max_chars=2))

        with allure.step('Проверить, что отображается валидация поля никнейм: '
                         '"- длина от 3 до 16 символов;'
                         ' - только английские буквы;'
                         ' - можно цифры;'
                         ' - можно точку (только в середине), дефис, нижнее подчеркивание;'
                         ' - нельзя использовать пробелы."'):
            self.assertion.text_in_element(element['Валидация поля никнейм'],
                                           expected_text='- длина от 3 до 16 символов; '
                                                         '- только английские буквы; '
                                                         '- можно цифры; '
                                                         '- можно точку (только в середине), дефис, нижнее подчеркивание; '
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

        with allure.step('В поле никнейм ввести более 16 символов'):
            self.join_page.field_send_keys(element['Поле никнейм'], text=fake.pystr(min_chars=17, max_chars=32))

        with allure.step('Проверить, что в поле введено не более 16 символов'):
            self.assertion.text_in_element_length(element['Поле никнейм'], length=16)

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
            self.join_page.field_send_keys(element['Поле никнейм'], text=fakeru.pystr(min_chars=3, max_chars=16))

        with allure.step('Проверить, что отображается валидация поля никнейм: '
                         '"- длина от 3 до 16 символов;'
                         ' - только английские буквы;'
                         ' - можно цифры;'
                         ' - можно точку (только в середине), дефис, нижнее подчеркивание;'
                         ' - нельзя использовать пробелы."'):
            self.assertion.text_in_element(element['Валидация поля никнейм'],
                                           expected_text='- длина от 3 до 16 символов; '
                                                         '- только английские буквы; '
                                                         '- можно цифры; '
                                                         '- можно точку (только в середине), дефис, нижнее подчеркивание; '
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
                                           expected_text='- длина от 3 до 16 символов; '
                                                         '- только английские буквы; '
                                                         '- можно цифры; '
                                                         '- можно точку (только в середине), дефис, нижнее подчеркивание; '
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
