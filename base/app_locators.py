from config.locators import *


class Locators:
    """ Класс с локаторами страниц """

    elements = {
        'Страница авторизации': AuthorizationPageLocators.locators,
        'Страница логина': LoginPageLocators.locators,
        'Страница регистрации': JoinPageLocators.locators,
        'Страница восстановления пароля': ResetPasswordPageLocators.locators,
        'Панель навигации': AppNavigationLocators.locators,
        'Профиль пользователя': ProfileLocatorsPageLocators.locators,
        'Банк ачивок': BankAchievementsPageLocators.locators,

    }
