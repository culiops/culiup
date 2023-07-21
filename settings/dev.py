from .base import *
import os

DEBUG = True
APP_VERSION = "0.1.0"
APP_ENV = "dev"
APP_NAME = "culiup"
APP_DOMAIN = "culiup.xyz"
BASE_URL = "https://dev.culiup.xyz"
ALLOWED_HOSTS = ["127.0.0.1", "dev.culiup.xyz", "localhost"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "uptime",
    "authen",
    "home",
    "corsheaders",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["DATABASE_NAME"],
        "USER": os.environ["DATABASE_USER"],
        "PASSWORD": os.environ["DATABASE_PASSWORD"],
        "HOST": os.getenv("DATABASE_HOST", "localhost"),
        "PORT": int(os.getenv("DATABASE_PORT", 5432)),
    }
}

MEDIA_ROOT = "/var/www/files/"
MEDIA_URL = BASE_URL + "/files/"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "verbose"}},
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

SECRET_KEY = os.environ["SECRET_KEY"]
CSRF_TRUSTED_ORIGINS = ["%s" % BASE_URL]
CORS_ALLOWED_ORIGINS = ["http://localhost", "http://127.0.0.1"]
CORS_ALLOW_CREDENTIALS = True

# CELERY_BROKER_URL = 'redis://redis:6379'
# ANSIBLE_RETRIES = 0
# PLAYBOOK_VERSION = "v2"
# COMMANDER_SSH_USERNAME = APP_NAME

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('redis', 6379)],
#         },
#     },
# }
