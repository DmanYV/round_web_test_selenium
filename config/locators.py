from selenium.webdriver.common.by import By


class AllPageLocators:
    """Локаторы присущие всем страницам"""
    # Спинер загрузки
    SPINNER = (By.XPATH, './/div[@class="spinner_rotating-plane__1g-WO"]')


class AuthorizationPageLocators:
    """Локаторы страницы Авторизации"""
    locators = {
        'Кнопка закрыть': (By.XPATH, './/button[@class="header_back__yUNba"]'),
        'Кнопка кэррот': (By.XPATH, '//div[@class="header_info__CHSYI"]'),
        'Кнопка по смс': (By.XPATH, '//button[@name="signUpWithSMS"]'),
        'Кнопка вконтакте': (By.XPATH, '//button[@name="signUpWithVK"]'),
        'Кнопка войти': (By.XPATH, './/a[text()="Войти"]'),
        'Кнопка лицензионная политика': (By.XPATH, '//a[@href="/license-policy"]'),

    }


class JoinPageLocators:
    """Локаторы страницы Регистрации"""
    locators = {
        'Кнопка далее': (By.XPATH, '//button[@class="button_content__7wfbm button_primary__tgW0W"]'),
        'Поле никнейм': (By.XPATH, '//input[@name="nickname"]'),
        'Поле пароль': (By.XPATH, '//input[@name="password"]'),
        'Поле повтори пароль': (By.XPATH, '//input[contains(@name,"passwordRepeat")]'),
        'Поле номер телефона': (By.XPATH, '//input[@name="phone"]'),
        'Поле проверочный код': (By.XPATH, '//input[@name="code"]'),
        'Текст приветствия пользователя': (By.XPATH, '//div[@class="registration-success_header__D5-xJ"]'),

    }


class LoginPageLocators:
    """Локаторы страницы Логина"""
    locators = {
        'Поле логин': (By.XPATH, './/input[@name="username"]'),
        'Поле пароль': (By.XPATH, './/input[@name="password"]'),
        'Валидация поля логин': (By.XPATH, './/div[@class = "text-field_container__vUCqA"][1]'
                                           '//label[@class = "text-field_validation-message__nizJJ"]'),
        'Валидация поля пароль': (By.XPATH, './/div[@class = "text-field_container__vUCqA"][2]'
                                            '//label[@class = "text-field_validation-message__nizJJ"]'),
        'Кнопка войти': (By.XPATH, './/button[text()="Войти"]'),
        'Кнопка закрыть': (By.XPATH, './/button[contains(@class, "header_back")]'),
        'Кнопка забыл пароль': (By.XPATH, './/div[text()="Забыл(-а) пароль?"]'),

    }


class MainPageLocators:
    """Локаторы страницы Главной"""


class RubricPageLocators:
    """Локаторы страницы Рубрики"""
