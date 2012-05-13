# -*- coding: utf-8 -*-
"""Heroku specific settings. These are used to deploy opencomparison to
Heroku's platform.
"""


from os import environ

from postgresify import postgresify

from settings.base import *


########## DATABASES
DATABASES = postgresify()


########## CACHE
CACHE_TIMEOUT = 60 * 60 * 24


########## WSGI SERVER
INSTALLED_APPS += ['gunicorn']


########## EMAIL
DEFAULT_FROM_EMAIL = environ.get('DEFAULT_FROM_EMAIL',
        'Django Packages <djangopackages-noreply@djangopackages.com>')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')
EMAIL_PORT = environ.get('EMAIL_PORT', 587)
EMAIL_SUBJECT_PREFIX = environ.get('EMAIL_SUBJECT_PREFIX', '[Django Packages] ')
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER


########## SECRET
SECRET_KEY = environ.get('SECRET_KEY', '')


ROOT_URLCONF = "app.urls"


GITHUB_API_SECRET = os.environ['GITHUB_API_SECRET']
GITHUB_APP_ID = os.environ['GITHUB_APP_ID']
SITE_TITLE = os.environ['SITE_TITLE']
FRAMEWORK_TITLE = os.environ['FRAMEWORK_TITLE']


########## STORAGE

INSTALLED_APPS += ['storages', ]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2020 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}

# Boto requires subdomain formatting.
from S3 import CallingFormat
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

# Amazon S3 configuration.
if os.environ.has_key('S3_KEY'):
    AWS_ACCESS_KEY_ID = os.environ['S3_KEY']
    AWS_SECRET_ACCESS_KEY = os.environ['S3_SECRET']
else:
    AWS_ACCESS_KEY_ID = AWS_KEY
    AWS_SECRET_ACCESS_KEY = AWS_SECRET_KEY

AWS_STORAGE_BUCKET_NAME = 'opencomparison'

STATIC_URL = 'https://s3.amazonaws.com/opencomparison/'
MEDIA_URL = STATIC_URL
########## END STORAGE CONFIGURATION
