import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class User:
    LOGIN = os.environ.get('LOGIN_USER')
    PASSWORD = os.environ.get('PASSWORD_USER')
    EMAIL = os.environ.get('EMAIL_USER')
    PHONE = os.environ.get('PHONE_USER')
