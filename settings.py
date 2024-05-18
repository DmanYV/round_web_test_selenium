import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


class User:
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
    EMAIL = os.getenv('EMAIL_USER')
    PHONE = os.getenv('PHONE_USER')
