import time

from base.base_page import BasePage


class DBRoundConfirmation(BasePage):
    PAGE_URL = None

    @staticmethod
    def get_last_sms_code(connection, time_wait: int = 2):
        """
        Получение последнего отправленного смс-кода из БД
        :param connection: Соединение с БД
        :param time_wait: Задержка в секундах перед получением последнего смс-кода (по умолчанию 2 секунда)

        :return: Последний отправленный смс-код
        """
        try:
            with connection.cursor() as cursor:
                time.sleep(time_wait)
                cursor.execute('SELECT "Code" FROM "ConfirmationCodes" ORDER BY "CreatedDate" DESC LIMIT 1;')
                last_sms_code = cursor.fetchone()
            if last_sms_code is not None:
                return last_sms_code[0]
            else:
                return None
        except Exception as error:
            print(f'Ошибка при получении последнего смс-кода из БД: {error}')
            return None
