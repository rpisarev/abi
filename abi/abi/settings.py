"""Settings for Zinnia Blog"""
import os
from os.path import abspath, basename, dirname, join, normpath
from sys import path

gettext = lambda s: s

DEBUG = True

DJANGO_ROOT = dirname(abspath(__file__))

SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)
path.append(DJANGO_ROOT)




DATABASES = {'default':
             {'ENGINE': 'django.db.backends.sqlite3',
              'NAME': normpath(join(SITE_ROOT, 'abi.db'))}
             }

TIME_ZONE = 'Europe/Kiev'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)
SECRET_KEY = 'jo-1rzm(%sf)3#n+fb7h955yu$3(pt63abhi12_t7e^^5q8dyw'

USE_TZ = True
USE_I18N = True
USE_L10N = True

SITE_ID = 1

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('en', ('English')),
    ('ru', ('Russian')),
)

LOCALE_PATHS = (
    os.path.join(dirname(__file__), 'locale'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'abi.urls'

TEMPLATE_DIRS = (
    os.path.join(dirname(__file__), 'templates').replace('\\','/'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'zinnia.context_processors.version',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'mptt',
    'zinnia',
    'tagging',
    'django_xmlrpc',
    'abinito',
    'portfolio',
    'event',
    'imagekit',
    'transmeta',
)

from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS
XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS
