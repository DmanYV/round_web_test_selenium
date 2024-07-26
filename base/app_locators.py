from config.locators import *


class Locators:
    """ Класс с локаторами страниц """

    elements = {
        'Общие': AllPageLocators.locators,
        'Панель навигации': AppNavigationLocators.locators,
        'Страница авторизации': AuthorizationPageLocators.locators,
        'Страница регистрации': JoinPageLocators.locators,
        'Страница логина': LoginPageLocators.locators,
        'Страница восстановления пароля': ResetPasswordPageLocators.locators,
        'Профиль пользователя': ProfileLocatorsPageLocators.locators,
        'Банк ачивок': BankAchievementsPageLocators.locators,
        'Модальное окно ачивки': AchievementModelWindowLocators.locators,
        'Главная страница': MainPageLocators.locators,
        'Страница рубрики': RubricPageLocators.locators,
    }
