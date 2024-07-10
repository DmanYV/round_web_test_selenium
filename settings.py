import os
from dotenv import load_dotenv

load_dotenv()


class User:
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
    EMAIL = os.getenv('EMAIL')
    PHONE = os.getenv('PHONE')
    INVCODE = os.getenv('INVCODE')


class MetaBaseUser:
    LOGIN = os.getenv('METABASELOGIN')
    PASSWORD = os.getenv('METABASEPASSWORD')
