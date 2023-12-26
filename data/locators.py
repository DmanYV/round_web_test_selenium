from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    """Локаторы страницы Авторизации"""
    # Кнопка 'Крестик'
    BUTTON_CLOSE = (By.XPATH, './/button[@class="header_back__yUNba"]')
    # Кнопка "Крротквенст"
    BUTTON_CARROT_QUEST = (By.XPATH, '//div[@class="header_info__CHSYI"]')
    # Кнопка войти По смс
    BUTTON_SMS_LOGIN = (By.XPATH, '//button[@name="signUpWithSMS"]')
    # Кнопка войти Вконтакте
    BUTTON_VK_LOGIN = (By.XPATH, '//button[@name="signUpWithVK"]')
    # Кнопка войти Email
    BUTTON_EMAIL_LOGIN = (By.XPATH, '//button[@name="signUpWithEmail"]')
    # Кнопка 'Войти'
    BUTTON_SIGN_IN = (By.XPATH, './/a[text()="Войти"]')
    # Кнопка Лицензионная политика
    BUTTON_LICENSED_SHELF = (By.XPATH, '//a[@href="/license-policy"]')


class LoginPageLocators:
    """Локаторы страницы Логина"""
    # Поле ввода 'Никнейм, email или номер телефона'
    FIELD_USERNAME = (By.XPATH, './/input[@name="username"]')
    # Поле ввода 'Пароль'
    FIELD_PASSWORD = (By.XPATH, './/input[@name="password"]')
    # Текст валидации поля 'Имя пользователя'
    VALIDATION_MESSAGE_USERNAME_FIELD = (
        By.XPATH, '//label[contains(.,"Введи e-mail, никнейм или номер телефона, указанные при регистрации")]')
    # Текст валидации поля 'Пароль'
    VALIDATION_MESSAGE_PASSWORD_FIELD = (By.XPATH, '//label[contains(.,"Введи пароль")]')
    # Кнопка 'Войти'
    BUTTON_SIGN_IN = (By.XPATH, './/button[text()="Войти"]')
    # Кнопка 'Крести\Закрыть'
    BUTTON_BACK = (By.XPATH, './/button[contains(@class, "header_back")]')
    # Кнопка 'Забыл(-а) пароль?'
    BUTTON_FORGO_PASSWORD = (By.XPATH, './/div[text()="Забыл(-а) пароль?"]')
    # ???
    SPINNER = (By.XPATH, './/div[@class="spinner_rotating-plane__1g-WO"]')
    # Попап с ошибкой авторизации
    POPUP_AUTH_ERROR = (By.XPATH, './/div[@class="popup_content__hyS0z"]')
