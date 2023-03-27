from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR        = Path(__file__).resolve().parent.parent
TEMPLATE_DIR    = os.path.join(BASE_DIR, "templates")
STATICFILES_DIR = os.path.join(BASE_DIR, "templates", "staticfiles")
MEDIA_DIR       = os.path.join(BASE_DIR, "templates", "staticfiles", "mediafiles")
STATIC_DIR      = os.path.join(BASE_DIR, "collectstatic")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY") #'django-insecure-xy615xc8+6lkd74)_2qn@+8zy96e061&ss@c^===*1=fr8xv+7'
DEBUG = config("DEBUG")
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'coreset.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'coreset.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL       = "static/"
STATICFILES_DIRS = (STATICFILES_DIR, )
STATIC_ROOT      = STATIC_DIR
MEDIA_URL        = "media/"
MEDIA_ROOT       = MEDIA_DIR

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'