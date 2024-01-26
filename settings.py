import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class User:
    login = os.environ.get('LOGIN_USER')
    password = os.environ.get('PASSWORD_USER')
    email = os.environ.get('EMAIL_USER')
    phone = os.environ.get('PHONE_USER')
