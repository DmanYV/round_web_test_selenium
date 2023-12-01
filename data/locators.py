from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    """Локаторы страницы Авторизации"""
    # Кнопка 'Крестик'
    BUTTON_CLOSE = (By.XPATH, './/button[@class="header_back__yUNba"]')
    # Кнопка 'Войти'
    BUTTON_SIGN_IN = (By.XPATH, './/a[text()="Войти"]')


class LoginPageLocators:
    """Локаторы страницы Логина"""
    # Поле ввода 'Никнейм, email или номер телефона'
    FIELD_USERNAME = (By.XPATH, './/input[@name="username"]')
    # Поле ввода 'Пароль'
    FIELD_PASSWORD = (By.XPATH, './/input[@name="password"]')
    # Кнопка 'Войти'
    BUTTON_SIGN_IN = (By.XPATH, './/button[text()="Войти"]')