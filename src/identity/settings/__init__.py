# -*- coding: utf-8 -*-
""" \file identity/settings/__init__.py
\brief Defines base project settings.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright © 2012 Concordus Applications, Inc.
           \n \n
           Permission is hereby granted, free of charge, to any person
           obtaining a copy of this software and associated documentation
           files (the "Software"), to deal in the Software without restriction,
           including without limitation the rights to use, copy, modify, merge,
           publish, distribute, sublicense, and/or sell copies of the Software,
           and to permit persons to whom the Software is furnished to do so,
           subject to the following conditions:
           \n \n
           The above copyright notice and this permission notice shall be
           included in all copies or substantial portions of the Software.
           \n \n
           THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
           EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
           MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
           NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
           BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
           ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
           CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
           SOFTWARE.
"""
from os import path
from django.core.urlresolvers import reverse
from django.conf import global_settings

# Project directories
PROJECT_NAME = 'identity'
PROJECT_ROOT = path.abspath(path.join(__file__, '..', '..'))

# Root directories
SITE_ROOT = path.abspath(path.join(PROJECT_ROOT, '..'))

# Debugging settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
TASTYPIE_FULL_DEBUG = DEBUG

# Forces debugging to false if server is accessed from an IP not listed here
INTERNAL_IPS = ('127.0.0.1',)

# Debugging tool bar configuration
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False}

# Site administrators; used for logging
ADMINS = ()

# Same as ADMINS but in a different group
MANAGERS = ADMINS

# Database configuration.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(SITE_ROOT, 'sqlite3.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '', }}

# Local time zone for this installation.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = ''

# URL prefix for static files.
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = ()

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '58yno^b5t^wvr)e4s8tet4&amp;#odp+9@+tu*nrq#*#d*gds%06w+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',)

# Middleware classes
MIDDLEWARE_CLASSES = ('django.middleware.gzip.GZipMiddleware',)

if DEBUG:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

MIDDLEWARE_CLASSES += (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',)

# Root URL configuration
ROOT_URLCONF = '{}.urls'.format(PROJECT_NAME)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{}.wsgi.application'.format(PROJECT_NAME)

# Template directories
TEMPLATE_DIRS = (
    path.join(PROJECT_ROOT, 'templates'))

# Installed applications
INSTALLED_APPS = (
    # Django core
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django administration
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Project
    PROJECT_NAME,

    # Accounts
    '{}.account'.format(PROJECT_NAME),)

if DEBUG:
    INSTALLED_APPS += (
        'django_extensions',
        'debug_toolbar',)

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {},
    'handlers': {},
    'loggers': {}}

# Define the extended user profile
AUTH_PROFILE_MODULE = 'account.Profile'

# Login settings
LOGIN_REDIRECT_URL = '/'

# Attempt to include local settings
try:
    from .local import *
except ImportError:
    pass
