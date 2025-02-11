from config.locators import *


class Locators:
    """ Класс с локаторами страниц """

    elements = {
        'Общие': AllPageLocators.locators,
        'Панель навигации': AppNavigationLocators.locators,
        'Страница авторизации': AuthorizationPageLocators.locators,
        'Кэррот': CarrotChatLocators.locators,
        'Страница регистрации': JoinPageLocators.locators,
        'Страница логина': LoginPageLocators.locators,
        'Страница восстановления пароля': ResetPasswordPageLocators.locators,
        'Профиль пользователя': ProfilePageLocators.locators,
        'Страница подписки': SubscriptionPageLocators.locators,
        'Банк ачивок': BankAchievementsPageLocators.locators,
        'Модальное окно ачивки': AchievementModelWindowLocators.locators,
        'Главная страница': MainPageLocators.locators,
        'Страница рубрики': RubricPageLocators.locators,
        'Поп ап бургер-меню профиля': PopUpBurgerMenuProfileLocators.locators,
        'Страница редактировать профиль': EditProfilePageLocators.locators,
        'Страница пригласить друга': InvitationPageLocators.locators,
        'Страница лайки': FavoriteProjectsPageLocators.locators,
        'Страница настройки аккаунта': SettingsPageLocators.locators,
        'Страница заблокированные пользователи': BlockListPageLocators.locators,
        'Страница другого пользователя': AnotherUserPageLocators.locators,
        'Глобальный поиск': GlobalSearchingPageLocators.locators
    }
