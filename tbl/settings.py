"""
Django settings for tbl project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from .config.apps import PRODUCTION_APPS, DEVELOPMENT_APPS
from .config.database import DB_DEVELOPMENT, DB_PRODUCTION
from .config.password import AUTH_PASSWORD_VALIDATORS
from .config.middleware import MIDDLEWARE
from .config.template import TEMPLATES
from .config.security import SECRET_KEY
from .config.files import (
    STATIC_ROOT, MEDIA_ROOT, STATIC_URL, MEDIA_URL
)
from .config.email import (
    DEFAULT_FROM_EMAIL, EMAIL_USE_TLS, EMAIL_HOST, EMAIL_HOST_USER,
    EMAIL_HOST_PASSWORD, EMAIL_PORT
)
from .config.user import (
    AUTH_USER_MODEL, LOGIN_URL, LOGOUT_URL, LOGIN_REDIRECT_URL,
    AUTHENTICATION_BACKENDS
)
from .config.internacionalization import (
    PORTUGUESE, ENGLISH, SAO_PAULO, USA, INTERNATIONALIZATION,
    FORMAT_DATES, TIMEZONE_DATETIMES
)
import os

# development or production enviroment
MODE_ENVIROMENT = os.getenv("MODE_ENVIROMENT", "development")

# Urls
ROOT_URLCONF = 'tbl.urls'

# WSGI - Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'tbl.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = PORTUGUESE
TIME_ZONE = SAO_PAULO
USE_I18N = INTERNATIONALIZATION
USE_L10N = FORMAT_DATES
USE_TZ = TIMEZONE_DATETIMES

# Enviroments mode (development or production)
if MODE_ENVIROMENT == 'development':
    DEBUG = True
    INSTALLED_APPS = DEVELOPMENT_APPS
    # Send email to console.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # Sqlite database
    DATABASES = DB_DEVELOPMENT
    # Allow all host/domain to access this aplication
    ALLOWED_HOSTS = ['*']

elif MODE_ENVIROMENT == 'production':
    DEBUG = False
    INSTALLED_APPS = PRODUCTION_APPS
    # Postgresql database
    DATABASES = DB_PRODUCTION
    # Send email to gmail
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # Allow all host/domain to access this aplication
    ALLOWED_HOSTS = ['*']
