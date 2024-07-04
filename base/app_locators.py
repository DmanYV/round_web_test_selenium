from config.locators import *


class Locators:
    """ Класс с локаторами страниц """

    elements = {
        'Страница авторизации': AuthorizationPageLocators.locators,
        'Страница логина': LoginPageLocators.locators,
        'Страница регистрации': JoinPageLocators.locators,
    }
