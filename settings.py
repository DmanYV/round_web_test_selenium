import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Aleska:
    login = os.environ.get('LOGIN_ADMINISTRATOR')
    password = os.environ.get('PASSWORD_ADMINISTRATOR')
    email = os.environ.get('EMAIL_ADMINISTRATOR')
    phone = os.environ.get('PHONE_ADMINISTRATOR')
