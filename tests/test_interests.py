import allure
import pytest
from faker import Faker

from base.base_test import BaseTest
from config.links import Links

fake = Faker()
fakeru = Faker("ru_RU")


@allure.feature('Интересы')
@pytest.mark.interests
class TestInterests(BaseTest):
    @allure.title('Присутствует информация о выборе "Интересов"')
    @allure.description('Проверка на регистрации нового пользователя')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_there_is_information_about_the_choice_of_interests(self, elements, db_connection):
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

        with allure.step('Получить смс код из Базы данных'):
            sms_code = self.db_round_confirmation.get_last_sms_code(db_connection)

        with allure.step('Ввести смс код'):
            self.login_page.field_send_keys(element['Поле проверочный код'], text=sms_code)

        with allure.step('Нажать кнопку погнали'):
            self.join_page.do_click(element['Кнопка погнали'])

        with allure.step('Закрыть велком видео'):
            self.join_page.do_click(element['Кнопка закрыть видео'])

        with allure.step('Проверить, что отображается список направлений'):
            element = elements['Страница рубрики']
            self.assertion.is_elem_displayed(element['Список интересов'])

    @allure.title('Возможность пропустить данный шаг без выбора "Интересов"')
    @allure.description('Проверка на регистрации нового пользователя')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_the_ability_to_skip_this_step_without_selecting_interests(self, elements, db_connection):
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

        with allure.step('Получить смс код из Базы данных'):
            sms_code = self.db_round_confirmation.get_last_sms_code(db_connection)

        with allure.step('Ввести смс код'):
            self.login_page.field_send_keys(element['Поле проверочный код'], text=sms_code)

        with allure.step('Нажать кнопку погнали'):
            self.join_page.do_click(element['Кнопка погнали'])

        with allure.step('Закрыть велком видео'):
            self.join_page.do_click(element['Кнопка закрыть видео'])

        with allure.step('Нажать кнопку "Выберу потом"'):
            element = elements['Страница рубрики']
            self.rubric_page.do_click(element['Кнопка выберу потом'])

        with allure.step('Проверить, что отображаются Список интересов и Подсказка Листай вниз'):
            element = elements['Главная страница']
            self.assertion.is_elem_displayed(element['Листай вниз и найди свои интересы'])
            self.assertion.is_elem_displayed(element['Список интересов'])

    @allure.title('Можно выбрать интересы')
    @allure.description('Проверка на регистрации нового пользователя')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_you_can_select_interests(self, elements, db_connection):
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

        with allure.step('Получить смс код из Базы данных'):
            sms_code = self.db_round_confirmation.get_last_sms_code(db_connection)

        with allure.step('Ввести смс код'):
            self.login_page.field_send_keys(element['Поле проверочный код'], text=sms_code)

        with allure.step('Нажать кнопку погнали'):
            self.join_page.do_click(element['Кнопка погнали'])

        with allure.step('Закрыть велком видео'):
            self.join_page.do_click(element['Кнопка закрыть видео'])

        with allure.step('Нажать на чипс с названием "Медиа"'):
            self.rubric_page.select_interest_by_name('Медиа')

        with allure.step('Проверить, что отображается кнопка "Классно! Перейти к подборке"'):
            element = elements['Страница рубрики']
            self.assertion.is_elem_displayed(element['Кнопка классно! перейти к подборке'])

    @allure.title('Кнопка "Классно! Перейти к подборке" кликабельна и перенаправляет на экран со скиллами')
    @allure.description('Проверка на регистрации нового пользователя')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_button_coolly_clickable_and_redirects_ti_the_screen_with_skills(self, elements, db_connection):
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

        with allure.step('Получить смс код из Базы данных'):
            sms_code = self.db_round_confirmation.get_last_sms_code(db_connection)

        with allure.step('Ввести смс код'):
            self.login_page.field_send_keys(element['Поле проверочный код'], text=sms_code)

        with allure.step('Нажать кнопку погнали'):
            self.join_page.do_click(element['Кнопка погнали'])

        with allure.step('Закрыть велком видео'):
            self.join_page.do_click(element['Кнопка закрыть видео'])

        with allure.step('Нажать на чипс с названием "Медиа"'):
            self.rubric_page.select_interest_by_name('Медиа')

        with allure.step('Проверить, что отображается кнопка "Классно! Перейти к подборке"'):
            element = elements['Страница рубрики']
            self.rubric_page.do_click(element['Кнопка классно! перейти к подборке'])

        with allure.step('Проверить, что отображается Листай вниз и найди свои интересы и Список интересов'):
            element = elements['Главная страница']
            self.assertion.is_elem_displayed(element['Листай вниз и найди свои интересы'])
            self.assertion.is_elem_displayed(element['Список интересов'])

    @allure.title('При клике "Все челледжи" происходит переход на страницу "Все челленджи"')
    @allure.description('Проверка на регистрации нового пользователя')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_pressing_the_all_challenges_button_opens_a_page_with_all_challenges(self, elements, login_to_app):
        element_main_page = elements['Главная страница']
        with allure.step('Нажать "Все челленджи"'):
            self.main_page.do_click(element_main_page['Все челленджи'])
        with allure.step('Проверить, что открылась страница челленджей'):
            self.assertion.page_is_opened(Links.CHALLENGE_PAGE)

    @allure.title('Проверка скролла чипсов')
    @allure.description('Проверка на пользователе Aleska')
    @allure.severity('Critical')
    @pytest.mark.regression
    def test_scrolling_chipsets(self, elements, login_to_app):
        element = elements['Чипсы']
        with allure.step('Проскролить чипсы в конец списка'):
            self.main_page.click_on_coordinates(1155,300)

        with allure.step('Проверить, что видим чипс с названием "Прибыльно" и нажать на него'):
            self.assertion.is_elem_displayed(element['Прибыльно'])
            chip = self.main_page.find_element(element['Прибыльно'])
            self.chips.do_click(chip)

