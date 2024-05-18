import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class User:
    LOGIN = os.getenv('LOGIN_USER')
    PASSWORD = os.getenv('PASSWORD_USER')
    EMAIL = os.environ.get('EMAIL_USER')
    PHONE = os.environ.get('PHONE_USER')
