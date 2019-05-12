import os

from dotenv import load_dotenv

from .base import (
    ALLOWED_HOSTS,
)
from .base import * # NOQA


load_dotenv()

DEBUG = False

ALLOWED_HOSTS += ['.pythonanywhere.com']

SECRET_KEY = os.getenv('SECRET_KEY')
