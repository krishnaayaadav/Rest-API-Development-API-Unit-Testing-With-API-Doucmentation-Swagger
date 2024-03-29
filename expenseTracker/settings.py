"""
Django settings for expenseTracker project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8bl#qkn-0e^svi%ojh&&@p=w(ucf^m9jtqk$#w9-=jc1x2^)bp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["restfulcrudapi.pythonanywhere.com", "*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "expenseApp",        # expenseApp
    "corsheaders",       # django-cors-headers for cors policy
    "rest_framework",    # rest_framework for develop rest-api
    "drf_spectacular",   # drf-spectaculr for api documentation
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # CORS Header Middleware
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'expenseTracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'expenseTracker.wsgi.application'


# MySQL Database Configured

DATABASES = {
   
   # development db here
   'default': {
      'ENGINE': 'django.db.backends.sqlite3',  # database engine
      'NAME':     BASE_DIR /'db.sqlite3'       # database name
   },
   
    # testing database here 
    'testing': {
        'ENGINE': 'django.db.backends.mysql',  # database engine
        'NAME': 'expense_db',                  # database name
        'HOST': 'localhost',                   # database host 
        'USER':  'root',                       # database user
        'PASSWORD': "",                        # database user password 
        "PORT": '3306',                        # database default port no
        "OPTIONS": {
            'sql_mode': 'STRICT_TRANS_TABLES'  # sql mode 

        }

    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and Mediafiles

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR /'static'

MEDIA_URL = '/media/'
MEDIA_ROOT= BASE_DIR /'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    
    # default renderer class as jsonrenderer
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    
    # default parser
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
     
    # default authentication classes
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
    ),
    # Default permission classes

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],

    # default response format for testing enviroment
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',

    
    # default schema class for api
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    
    # Throttling classes
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    
    # Throttle Rates
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}

# CORS Policy For Development Only
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',  # for django development server
    'http://localhost:3000',  # for react js origin request allowed

)

SPECTACULAR_SETTINGS = {
    'TITLE': 'DRF Expense Tracker API',
    'DESCRIPTION': 'Expense Tracker API. It is designed usign DjangoRestFramewrk, ORM, MySQL, SQLite3, Swagger for API documentation with dockerization. Project contains 3 main features as API development | API Testing | API Documentation Using Swagger. It contains different API Endpoints for Add New Expense, Get All Expenses, Get Expense Details, Update And Delete Particular Expense Item. ',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

# Caching System
CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
      'LOCATION': BASE_DIR /'sitecaches/django_cache',
   }
}