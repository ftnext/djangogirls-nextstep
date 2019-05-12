import os

from .base import (
    BASE_DIR, INSTALLED_APPS, MIDDLEWARE,
)
from .base import * # NOQA


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sowzp430a_%m@r+dye=x9-4i!c&s(mmuw-tvjf4i!$!4)2f1j('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = '127.0.0.1'


# Uploaded files

MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media_root')


# Email dummy

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
