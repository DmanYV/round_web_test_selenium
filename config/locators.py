from selenium.webdriver.common.by import By


class AppNavigationLocators:
    """Локаторы для навигации в приложении"""
    locators = {
        'Кнопка главная': (By.XPATH, '//a[@href="/"]'),
        'Кнопка лента': (By.XPATH, '//a[@href="/feed"]'),
        'Кнопка плюс': (By.XPATH, '//a[@href="/newbie"]'),
        'Кнопка профиль': (By.XPATH, '//a[@href="/profile"]'),
        'Кнопка уведомления': (By.XPATH, '//a[@href="/notification"]')
    }


class AllPageLocators:
    """Локаторы присущие всем страницам"""

    locators = {
        'Спиннер загрузки': (By.XPATH, './/div[@class="spinner_rotating-plane__1g-WO"]'),
        'Заголовок страницы': (By.XPATH, '//div[contains(@class,"tool-bar_title")]'),
        'Кнопка назад': (By.XPATH, '//button[contains(@class,"tool-bar_back")]'),
    }


class AnotherUserPageLocators:
    """Локаторы страницы другого пользователя"""

    locators = {
        'Кнопка три точки': (By.XPATH, '//button[contains(@class,"profile-page-header_button")]'),
        'Пожаловаться': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_item")][contains(.,"Пожаловаться")]'),
        'Заблокировать': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_item")]'
                                    '[contains(.,"Заблокировать")]'),
        'Пользователь заблокирован': (By.XPATH, '//div[contains(@class,"user-in-blocklist-description_container")]'),
        'Разблокировать': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_item")]'
                                     '[contains(.,"Разблокировать")]'),
        'Кнопка подписаться': (By.XPATH, '//button[contains(@class,"button_primary")][contains(.,"Подписаться")]'),
        'Кнопка подписка': (By.XPATH, '//button[contains(@class,"button_light")][contains(.,"Подписка")]'),
        'Значок галочки': (By.XPATH, '//div[contains(@class,"page-content_content")]'
                                     '//div[contains(@class,"popup_container")]'),
        'Аватар': (By.XPATH, '//img[contains(@class,"user-info_icon")]'),
        'Список проектов': (By.XPATH, '//div[@class = "user-project-list_grid__-rXf1"]'
                                      '//div[@class = "user-project-list_item__Q1mmt"]'),
        'Блок ачивок': (By.XPATH, '(//div[contains(@class,"horizontal-scroll-view_container")])'
                                  '//div[contains(@class,"user-achievement-list_item")]'),
        'Подписки': (By.XPATH, '//div[@id="user-info_following"]'
                               '//div[contains(@class,"user-info_count")]'),
        'Спам': (By.XPATH, '//label[contains(.,"Спам")]'),
        'Нарушение авторского права, неоригинальный контент': (
            By.XPATH, '//label[contains(.,"Нарушение авторского права, неоригинальный контент")]'
        ),
        'Оскорбление, враждебные высказывания': (
            By.XPATH, '//label[contains(.,"Оскорбление, враждебные высказывания")]'
        ),
        'Материал для взрослых или действия сексуального характера': (
            By.XPATH, '//label[contains(.,"Материал для взрослых или действия сексуального характера")]'
        ),
        'Пропаганда наркотиков': (By.XPATH, '//label[contains(.,"Пропаганда наркотиков")]'),
        'Продажа оружия': (By.XPATH, '//label[contains(.,"Продажа оружия")]'),
        'Травля, преследование, призыв к травле или преследованию': (
            By.XPATH, '//label[contains(.,"Травля, преследование, призыв к травле или преследованию")]'
        ),
        'Призыв к суициду': (By.XPATH, '//label[contains(.,"Призыв к суициду")]'),
        'Жестокое обращение с животными': (By.XPATH, '//label[contains(.,"Жестокое обращение с животными")]'),
        'Введение в заблуждение': (By.XPATH, '//label[contains(.,"Введение в заблуждение")]'),
        'Мошенничество': (By.XPATH, '//label[contains(.,"Мошенничество")]'),
        'Насилие/экстремизм': (By.XPATH, '//label[contains(.,"Насилие/экстремизм")]'),
        'Другое': (By.XPATH, '//label[contains(.,"Другое")]'),
        'Кнопка пожаловаться': (By.XPATH, '//button[contains(@class,"message-dialog_secondary")]'),
        'Уведомление жалоба на пользователя отправлена': (
            By.XPATH, '//div[contains(@class,"popup_container")][contains(.,"Жалоба на пользователя отправлена")]'
        ),
        'Поле причина жалобы': (By.XPATH, '//input[contains(@class,"text-field_input")]')
    }


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


class CarrotChatLocators:
    """Локаторы окна кэррот чата"""
    locators = {
        'Фрейм кэррот': (By.ID, 'carrot-messenger-frame'),
        'Окно кэррот': (By.ID, 'carrotquest-messenger'),
        'Чат кэррот': (By.XPATH, '//div[contains(@class,"carrot-messenger-frame-container")]'),
    }


class JoinPageLocators:
    """Локаторы страницы регистрации"""
    locators = {
        'Кнопка далее': (By.XPATH, '//button[@class="button_content__7wfbm button_primary__tgW0W"]'),
        'Поле годов рождения': (By.XPATH, '//div[@class=" css-1dimb5e-singleValue"]'),
        'Список годов рождения': (By.ID, 'react-select-2-listbox'),
        'Поле никнейм': (By.XPATH, '//input[@name="nickname"]'),
        'Валидация поля никнейм': (By.XPATH, '//label[@class="text-field_validation-message__nizJJ"]'),
        'Поле пароль': (By.XPATH, '//input[@name="password"]'),
        'Валидация поля пароль': (By.XPATH, '//label[@class="text-field_validation-message__nizJJ"]'),
        'Поле повтори пароль': (By.XPATH, '//input[contains(@name,"passwordRepeat")]'),
        'Валидация поля повтори пароль': (By.XPATH, '//label[@class="text-field_validation-message__nizJJ"]'),
        'Чекбокс код приглашения': (By.XPATH, '//label[contains(@class,"kkh2y")]'),
        'Поле код приглашения': (By.XPATH, '//input[@name="referralCode"]'),
        'Валидация поля код приглашения': (By.XPATH, '//label[@class="text-field_validation-message__nizJJ"]'),
        'Поле номер телефона': (By.XPATH, '//input[@name="phone"]'),
        'Валидация поля номер телефона': (By.XPATH, '//div[contains(@class,"kPIDC")]'),
        'Поле проверочный код': (By.XPATH, '//input[@name="code"]'),
        'Валидация поля проверочный код': (By.XPATH, '//label[@class="phone-screen_confirm-error__q-TwZ"]'),
        'Текст приветствия пользователя': (By.XPATH, '//div[contains(@class,"registration-success_header_")]'),
        'Кнопка запросить код еще раз': (By.XPATH, '//button[contains(@class,"j7a6Y")]'),
        'Кнопка погнали': (By.XPATH, '//button[contains(@class,"registration-success_btn")]'),
        '2014 год': (By.ID, 'react-select-2-option-0'),
        '2013 год': (By.ID, 'react-select-2-option-1'),
        '2012 год': (By.ID, 'react-select-2-option-2'),
        '2011 год': (By.ID, 'react-select-2-option-3'),
        '2010 год': (By.ID, 'react-select-2-option-4'),
        '2009 год': (By.ID, 'react-select-2-option-5'),
        '2008 год': (By.ID, 'react-select-2-option-6'),
        '2007 год': (By.ID, 'react-select-2-option-7'),
        '2006 год': (By.ID, 'react-select-2-option-8'),
        '2005 год': (By.ID, 'react-select-2-option-9'),
        '2004 год': (By.ID, 'react-select-2-option-10'),
        '2003 год': (By.ID, 'react-select-2-option-11'),
        '2002 год': (By.ID, 'react-select-2-option-12'),
        '2001 год': (By.ID, 'react-select-2-option-13'),
        '2000 год': (By.ID, 'react-select-2-option-14'),
        '1999 год': (By.ID, 'react-select-2-option-15'),
        '1998 год': (By.ID, 'react-select-2-option-16'),
        '1997 год': (By.ID, 'react-select-2-option-17'),
        '1996 год': (By.ID, 'react-select-2-option-18'),
        '1995 год': (By.ID, 'react-select-2-option-19'),
        '1994 год': (By.ID, 'react-select-2-option-20'),
        '1993 год': (By.ID, 'react-select-2-option-21'),
        '1992 год': (By.ID, 'react-select-2-option-22'),
        '1991 год': (By.ID, 'react-select-2-option-23'),
        '1990 год': (By.ID, 'react-select-2-option-24'),
        '1989 год': (By.ID, 'react-select-2-option-25'),
        '1988 год': (By.ID, 'react-select-2-option-26'),
        '1987 год': (By.ID, 'react-select-2-option-27'),
        '1986 год': (By.ID, 'react-select-2-option-28'),
        '1985 год': (By.ID, 'react-select-2-option-29'),
        '1984 год': (By.ID, 'react-select-2-option-30'),
        '1983 год': (By.ID, 'react-select-2-option-31'),
        '1982 год': (By.ID, 'react-select-2-option-32'),
        '1981 год': (By.ID, 'react-select-2-option-33'),
        '1980 год': (By.ID, 'react-select-2-option-34'),
        '1979 год': (By.ID, 'react-select-2-option-35'),
        '1978 год': (By.ID, 'react-select-2-option-36'),
        '1977 год': (By.ID, 'react-select-2-option-37'),
        '1976 год': (By.ID, 'react-select-2-option-38'),
        '1975 год': (By.ID, 'react-select-2-option-39'),
        '1974 год': (By.ID, 'react-select-2-option-40'),
        '1973 год': (By.ID, 'react-select-2-option-41'),
        '1972 год': (By.ID, 'react-select-2-option-42'),
        '1971 год': (By.ID, 'react-select-2-option-43'),
        '1970 год': (By.ID, 'react-select-2-option-44'),
        '1969 год': (By.ID, 'react-select-2-option-45'),
        '1968 год': (By.ID, 'react-select-2-option-46'),
        '1967 год': (By.ID, 'react-select-2-option-47'),
        '1966 год': (By.ID, 'react-select-2-option-48'),
        '1965 год': (By.ID, 'react-select-2-option-49'),
        '1964 год': (By.ID, 'react-select-2-option-50'),
        '1963 год': (By.ID, 'react-select-2-option-51'),
        '1962 год': (By.ID, 'react-select-2-option-52'),
        '1961 год': (By.ID, 'react-select-2-option-53'),
        '1960 год': (By.ID, 'react-select-2-option-54'),
        '1959 год': (By.ID, 'react-select-2-option-55'),
        '1958 год': (By.ID, 'react-select-2-option-56'),
        '1957 год': (By.ID, 'react-select-2-option-57'),
        '1956 год': (By.ID, 'react-select-2-option-58'),
        '1955 год': (By.ID, 'react-select-2-option-59'),
        '1954 год': (By.ID, 'react-select-2-option-60'),
        '1953 год': (By.ID, 'react-select-2-option-61'),
        '1952 год': (By.ID, 'react-select-2-option-62'),
        '1951 год': (By.ID, 'react-select-2-option-63'),
        '1950 год': (By.ID, 'react-select-2-option-64'),
        '1949 год': (By.ID, 'react-select-2-option-65'),
        '1948 год': (By.ID, 'react-select-2-option-66'),
        '1947 год': (By.ID, 'react-select-2-option-67'),
        '1946 год': (By.ID, 'react-select-2-option-68'),
        '1945 год': (By.ID, 'react-select-2-option-69'),
        '1944 год': (By.ID, 'react-select-2-option-70'),
        '1943 год': (By.ID, 'react-select-2-option-71'),
        '1942 год': (By.ID, 'react-select-2-option-72'),
        '1941 год': (By.ID, 'react-select-2-option-73'),
        '1940 год': (By.ID, 'react-select-2-option-74'),
        '1939 год': (By.ID, 'react-select-2-option-75'),
        '1938 год': (By.ID, 'react-select-2-option-76'),
        '1937 год': (By.ID, 'react-select-2-option-77'),
        '1936 год': (By.ID, 'react-select-2-option-78'),
        '1935 год': (By.ID, 'react-select-2-option-79'),
        '1934 год': (By.ID, 'react-select-2-option-80'),
        '1933 год': (By.ID, 'react-select-2-option-81'),
        '1932 год': (By.ID, 'react-select-2-option-82'),
        '1931 год': (By.ID, 'react-select-2-option-83'),
        '1930 год': (By.ID, 'react-select-2-option-84'),
        '1929 год': (By.ID, 'react-select-2-option-85'),
        '1928 год': (By.ID, 'react-select-2-option-86'),
        '1927 год': (By.ID, 'react-select-2-option-87'),
        '1926 год': (By.ID, 'react-select-2-option-88'),
        '1925 год': (By.ID, 'react-select-2-option-89'),

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
        'Кнопка забыл пароль': (By.XPATH, '//div[@class="login_restore-link__lQcSj"]'),
        'Уведомление аккаунт удален': (By.XPATH, '//div[contains(@class,"popup_container")]')
    }


class ResetPasswordPageLocators:
    """Страница восстановления пароля"""
    locators = {
        'Поле логин': (By.XPATH, '//input[@name="login"]'),
        'Валидация поля логин': (By.XPATH, '//div[@class="reset-login-form_error__9yjIT"]'),
        'Кнопка сбросить пароль': (By.XPATH, '//button[@class="button_content__7wfbm button_primary__tgW0W"]'),
        'Поле код из письма': (By.XPATH, '//input[@name="code"]'),
        'Поле код из смс': (By.XPATH, '//input[@name="code"]'),
        'Валидация поля код из смс': (By.XPATH, '//label[@class="text-field_validation-message__nizJJ"]'),
        'Поле пароль': (By.XPATH, '//input[@name="password"]'),
        'Поле повтори пароль': (By.XPATH, '//input[@name="passwordRepeat"]'),
        'Кнопка сохранить': (By.XPATH, '//button[@class="button_content__7wfbm button_primary__tgW0W"]'),
        'Кнопка хорошо': (By.XPATH, '//button[@class="message-dialog_primary__p6nDx"]'),
        'Диалоговое окно пароль изменен': (By.XPATH, '//div[@class="message-dialog_text__FBuOm"]'),
        'Кнопка запросить код еще раз': (By.XPATH, '//button[@class="button_content__7wfbm button_light__j7a6Y"]')

    }


class ProfilePageLocators:
    """Локаторы страницы профиля"""
    locators = {
        'Никнейм пользователя': (By.XPATH, '//div[@class="tool-bar_title__4eJyZ"]'),
        'Аватар': (By.XPATH, '//img[contains(@class,"user-info_icon")]'),
        'Проекты': (By.XPATH, '//div[@id="user-info_projects"]'
                              '//div[contains(@class,"user-info_count")]'),
        'Подписчики': (By.XPATH, '//div[@id="user-info_followers"]'
                                 '//div[contains(@class,"user-info_count")]'),
        'Подписки': (By.XPATH, '//div[@id="user-info_following"]'
                               '//div[contains(@class,"user-info_count")]'),
        'О себе': (By.XPATH, '//div[contains(@class,"user-info_about")]'),
        'Список проектов': (By.XPATH, '//div[@class = "user-project-list_grid__-rXf1"]'
                                      '//div[@class = "user-project-list_item__Q1mmt"]'),
        'Проект ожидает модерации': (By.XPATH, '//div[contains(@class,"user-project-list_moderation")]'),
        'Проект заблокирован': (By.XPATH, '//div[contains(@class,"user-project-list_blocked")]'),
        'Счетчик просмотров проекта': (By.XPATH, '//div[@class="user-project-list_count__TcOiJ"]'),
        'Кнопка все': (By.XPATH, '//div[contains(@class,"user-achievement-list_all")]'),
        'Блок ачивок': (By.XPATH, '(//div[contains(@class,"horizontal-scroll-view_container")])'
                                  '//div[contains(@class,"user-achievement-list_item")]'),
        'Кнопка бургер-меню': (By.XPATH, '//button[contains(@class,"profile-page-header_button")]'),
        'Поп ап бургер-меню': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_content")]'),
        'Кнопка закрыть анкету': (By.XPATH, '//div[contains(@class,"study-choose_container")]//*[local-name() = "svg"]')
    }


class SubscriptionPageLocators:
    """Локаторы страницы подписки"""
    locators = {
        'Подписчики': (By.XPATH, '//button[@tabindex="0"]'),
        'Подписки': (By.XPATH, '//button[@tabindex="1"]'),
        'Все пользователи': (By.XPATH, '//button[@tabindex="2"]'),
        'Список пользователей': (By.XPATH, '//div[contains(@class,"user-block_container")]'),
        'Подписка на первого пользователя': (By.XPATH, '//button[contains(.,"Подписаться")][1]'),
        'Отписка от первого пользователя': (By.XPATH, '//button[contains(.,"Подписка")][1]'),
        'Значок галочки': (By.XPATH, '//div[contains(@class,"popup_container")]'),
    }


class PopUpBurgerMenuProfileLocators:
    """Локаторы поп ап бургер-меню профиля"""
    locators = {
        'Редактировать профиль': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_content")]'
                                            '//div[contains(.,"Редактировать профиль")]'),
        'Пригласить друга': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_content")]'
                                       '//div[contains(.,"Пригласить друга")]'),
        'Лайки': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_content")]'
                            '//div[contains(.,"Лайки")]'),
        'Избранное': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_content")]'
                                '//div[contains(.,"Избранное")]'),
        'Тех. поддержка': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_content")]'
                                     '//div[contains(.,"Тех. поддержка")]'),
        'О системе': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_content")]'
                                '//div[contains(.,"О системе")]'),
        'Выйти из аккаунта': (By.XPATH, '//div[contains(@class,"popup-dialog-fragment_content")]'
                                        '//div[contains(.,"Выйти из аккаунта")]'),



    }


class FavoriteProjectsPageLocators:
    """Локаторы страницы Лайки"""
    locators = {

    }


class FavoriteChallengePage:
    """Локаторы страницы Избранное"""
    locators = {

    }


class InvitationPageLocators:
    """Локаторы страницы пригласить друга"""
    locators = {
        'Заголовок страницы': (By.XPATH, '//div[contains(@class,"profile-invitation_title")]'),
    }


class EditProfilePageLocators:
    """Локаторы страницы редактировать профиль"""
    locators = {
        'Поле никнейм': (By.XPATH, '//input[@name="userName"]'),
        'Поле о себе': (By.XPATH, '//textarea[@name="about"]'),
        'Кнопка сохранить': (By.XPATH, '//button[contains(@class,"button_primary")]'),
        'Поп ап уведомление': (By.XPATH, '//div[contains(@class, "popup_container")]'),
        'Анкета': (By.XPATH, '//button[contains(@class,"profile-edit-button_container")][contains(.,"Анкета")]'),
        'Настройки аккаунта': (By.XPATH, '//button[contains(@class,"profile-edit-button_container")]'
                                         '[contains(.,"Настройки аккаунта")]'),
        'Заблокированные пользователи': (By.XPATH, '//button[contains(@class,"profile-edit-button_container")]'
                                                   '[contains(.,"Заблокированные пользователи")]'),
        'Кнопка добавить аватар': (By.XPATH, '//input[@type="file"]'),
        'Кнопка хорошо': (By.XPATH, '//button[contains(.,"Хорошо")]')
    }


class SettingsPageLocators:
    """Локаторы страницы Настройки аккаунта"""
    locators = {
        'Удалить аккаунт': (By.XPATH, '//div[contains(@class,"user-settings_line")]'),
        'Кнопка удалить': (By.XPATH, '//button[contains(@class,"message-dialog_secondary")]'),
        'Кнопка отмена': (By.XPATH, '//button[contains(@class,"message-dialog_primary")]'),
        'У меня есть другой профиль в ROUND!': (By.XPATH, '//label[contains(.,"У меня есть другой профиль в ROUND!")]'),
        'Мои проекты не комментируют и не лайкают': (By.XPATH, '//label[contains(.,"Мои проекты не комментируют и не лайкают")]'),
        'Ведение аккаунта отнимает у меня много времени': (By.XPATH, '//label[contains(.,"Ведение аккаунта отнимает у меня много времени")]'),
        'Не нашел (-ла) интересного для себя контента': (By.XPATH, '//label[contains(.,"Не нашел (-ла) интересного для себя контента")]'),
        'Удаляю по просьбе родителей': (By.XPATH, '//label[contains(.,"Удаляю по просьбе родителей")]'),
        'Меня беспокоит безопасность моих данных': (By.XPATH, '//label[contains(.,"Меня беспокоит безопасность моих данных")]'),
        'Другая причина': (By.XPATH, '//label[contains(.,"Другая причина")]'),
        'Поле причина удаления': (By.XPATH, '//input[contains(@class,"text-field_input")]'),
        'Кнопка удалить аккаунт': (By.XPATH, '//button[contains(@class,"message-dialog_secondary")]'),
        'Уведомление пользователя': (By.XPATH, '//div[contains(@class,"message-dialog_text")]'),
        'Кнопка хорошо': (By.XPATH, '//button[contains(@class,"message-dialog_primary")]')
    }


class BlockListPageLocators:
    """Локаторы страницы Заблокированные пользователи"""
    locators = {
        'Список пуст': (By.XPATH, '//div[contains(@class,"user-block-list_empty")]'),
        'Список заблокированных пользователей': (By.XPATH, '//div[contains(@class,"user-block-list_block")]'),
        'Кнопка разблокировать': (By.XPATH, '//button[contains(@class,"user-block-list_link")]'
                                            '[contains(.,"Разблокировать")]')
    }


class BankAchievementsPageLocators:
    """Локаторы страницы Банк ачивок"""
    locators = {
        'Блок ачивок': (By.XPATH, '//div[contains(@class,"user-achievement-by-interests_container")]'),
        'Модальное окно ачивки': (By.XPATH, '//div[contains(@class,"app-container_container")]')
    }


class AchievementModelWindowLocators:
    """Локаторы модального окна ачивки"""
    locators = {
        'Название ачивки': (By.XPATH, '//div[contains(@class,"achievement-item-bottom-sheet_title")]'),
        'Аватары у кого есть эта ачивка': (By.XPATH, '//div[contains(@class,"achievement-item-bottom-sheet_icons")]')
    }


class MainPageLocators:
    """Локаторы страницы Главной"""
    locators = {
        'Листай вниз и найди свои интересы': (By.XPATH, '//div[@class="onboarding_container__mDp2D"]')
    }


class RubricPageLocators:
    """Локаторы страницы Рубрики"""
    locators = {
        'Кнопка выберу потом': (By.XPATH, '//button[@class="button_content__7wfbm button_light__j7a6Y"]')
    }
