"""
Django settings for paw_rescue project.
"""

from pathlib import Path
import os
import dj_database_url

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key secret!
SECRET_KEY = 'django-insecure-8f4t!$3&4qgpjoor-c7xp4sk+*jkp-7vf4%x35$ah1o!g$2a)f'

# Debug (❌ Set to False in production)
DEBUG = True

# Allow all hosts (for Render)
ALLOWED_HOSTS = ["*"]

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your apps
    'accounts',
    'feed',
    'adminpanel',

    # cloudinary
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'paw_rescue.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'paw_rescue.wsgi.application'


# Database (Neon PostgreSQL)
DATABASES = {
    "default": dj_database_url.config(
        default="postgresql://neondb_owner:npg_bGguxX0VRQ7w@ep-green-brook-adn3o7bq-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require"
    )
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ---------------- Static & Media ----------------

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files → stored in Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dhol8imhb',
    'API_KEY': '616112266455922',
    'API_SECRET': 'LVW7RCMdSQzSFQHrP5di_K58p4w',
}

MEDIA_URL = 'https://res.cloudinary.com/dhol8imhb/'
  # still works, but files served from Cloudinary

# ------------------------------------------------

# Default PK field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect after login
LOGIN_REDIRECT_URL = '/feed/'
