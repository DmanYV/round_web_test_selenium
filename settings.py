import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class User:
    LOGIN = os.getenv('LOGIN_USER')
    PASSWORD = os.getenv('PASSWORD_USER')
    EMAIL = os.getenv('EMAIL_USER')
    PHONE = os.getenv('PHONE_USER')
