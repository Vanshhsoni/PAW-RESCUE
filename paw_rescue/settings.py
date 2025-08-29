"""
Django settings for paw_rescue project.
"""
from pathlib import Path
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ------------------------
# BASE DIRECTORY
# ------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------
# SECURITY
# ------------------------
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-8f4t!$3&4qgpjoor-c7xp4sk+*jkp-7vf4%x35$ah1o!g$2a)f')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
ALLOWED_HOSTS = ["*"]  # allow all hosts for Render deployment

# ------------------------
# INSTALLED APPS
# ------------------------
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Cloudinary apps (order is important - cloudinary_storage must come first)
    'cloudinary_storage',
    'cloudinary',
    
    # Your apps
    'accounts',
    'feed',
    'adminpanel',
    'payment',
]

# ------------------------
# MIDDLEWARE
# ------------------------
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

# ------------------------
# URLS & TEMPLATES
# ------------------------
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

# ------------------------
# PAYMENTS
# ------------------------

RAZORPAY_KEY_ID = "rzp_live_RB48amAw3o864Z"
RAZORPAY_KEY_SECRET = "s7sOEEAW1lRirmd87VYgaahL"

# ------------------------
# DATABASE (PostgreSQL Neon)
# ------------------------
DATABASES = {
    "default": dj_database_url.parse(
        os.getenv('DATABASE_URL', 
            "postgresql://neondb_owner:npg_bGguxX0VRQ7w@ep-green-brook-adn3o7bq-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
        ),
        conn_max_age=600,
        ssl_require=True,
    )
}

# ------------------------
# PASSWORD VALIDATION
# ------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------
# INTERNATIONALIZATION
# ------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------
# STATIC FILES
# ------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ------------------------
# CLOUDINARY CONFIGURATION
# ------------------------
# Cloudinary credentials (use environment variables in production)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME', 'dhol8imhb'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY', '616112266455922'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', 'LVW7RCMdSQzSFQHrP5di_K58p4w'),
}

# Configure cloudinary
cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET'],
    secure=True
)

# ------------------------
# MEDIA FILES (Cloudinary)
# ------------------------
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

# File upload settings
FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024   # 10MB

# ------------------------
# LOGGING (Optional - for debugging uploads)
# ------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'cloudinary': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

# ------------------------
# DEFAULT PK & LOGIN
# ------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/feed/'

# ------------------------
# SECURITY SETTINGS (Production)
# ------------------------
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = 'DENY'
    
# ------------------------
# CSRF SETTINGS
# ------------------------
CSRF_TRUSTED_ORIGINS = [
    'https://*.render.com',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
