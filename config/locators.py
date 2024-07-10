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
        'Фрейм кэррот': (By.ID, 'carrot-messenger-frame'),
        'Окно кэррот': (By.ID, 'carrotquest-messenger'),
        'Кнопка по смс': (By.XPATH, '//button[@name="signUpWithSMS"]'),
        'Кнопка вконтакте': (By.XPATH, '//button[@name="signUpWithVK"]'),
        'Кнопка войти': (By.XPATH, './/a[text()="Войти"]'),
        'Кнопка лицензионная политика': (By.XPATH, '//a[@href="/license-policy"]'),

    }


class JoinPageLocators:
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
        'Кнопка забыл пароль': (By.XPATH, './/div[text()="Забыл(-а) пароль?"]'),

    }


class MainPageLocators:
    """Локаторы страницы Главной"""


class RubricPageLocators:
    """Локаторы страницы Рубрики"""
