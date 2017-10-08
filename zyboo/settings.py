"""
Django settings for zyboo project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w)6^gr(oa^je$p9l!@t+lw^9%0!s(11@*c6=)-uvb2&rmt473v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['zyboo.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'zybooEvents',
    'floppyforms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zyboo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['zyboo',],
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

WSGI_APPLICATION = 'zyboo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'zyboo',
        'USER': 'zyboouser',
        'PASSWORD': 'zyboouser',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# GEOIP_PATH = BASE_DIR + '/geoip'


GDAL_LIBRARY_PATH = '/app/.heroku/vendor/lib/libgdal.so'
GEOS_LIBRARY_PATH = '/app/.heroku/vendor/lib/libgeos_c.so'
# GEOIP_LIBRARY_PATH = '/app/.heroku/python/lib/python3.6/site-packages/django/contrib/gis/geoip/libgeoip.pyo'

GEOIP_GEOLITE2_PATH = '/app/.heroku/vendor/lib/share'
GEOIP_GEOLITE2_CITY_FILENAME = 'GeoLite2-City.mmdb'
GEOIP_GEOLITE2_COUNTRY_FILENAME = 'GeoLite2-Country.mmdb'

GEOIP_PATH=os.environ['GEOIP_GEOLITE2_PATH']
GEOIP_CITY=os.environ['GEOIP_GEOLITE2_CITY_FILENAME']
GEOIP_COUNTRY=os.environ['GEOIP_GEOLITE2_COUNTRY_FILENAME']

# Copy libjasper since it's only available in heroku buildenv
# cp /usr/lib/x86_64-linux-gnu/libjasper.so* "$BUILD_DIR/$TARGET_VENDOR_DIR/lib/."
# cp /Users/nirav/IdeaProjects/zyboo/dependency-heroku/libjasper.so* "/app/.heroku/vendor/lib/."


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = "staticfiles"
STATIC_URL = '/static/'