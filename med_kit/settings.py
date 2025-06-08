import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
# Pull SECRET_KEY and DEBUG from env, with safe defaults for local development
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-local-fallback-key')
DEBUG = os.environ.get('DEBUG', 'True') != 'False'

# Hosts
ALLOWED_HOSTS = os.environ.get(
    'ALLOWED_HOSTS',
    'localhost,127.0.0.1,your-app.herokuapp.com,yourdomain.com'
).split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_home',
    'app_med_kit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serve static files on Heroku
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'med_kit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # add any project-level template dirs here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'med_kit.wsgi.application'


# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get(
            'DATABASE_URL',
            f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
        ),
        conn_max_age=600,
        ssl_require=not DEBUG
    )
}


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'  # change if you need a different TZ
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Where collectstatic will collect to
STATIC_ROOT = BASE_DIR / 'staticfiles'

# For local development, also look here
STATICFILES_DIRS = [BASE_DIR / 'static']

# WhiteNoise storage backend for proper caching & compression
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirects after login/logout
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'
