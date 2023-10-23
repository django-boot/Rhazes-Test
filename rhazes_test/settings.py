import os

from django.conf.global_settings import DATETIME_INPUT_FORMATS
from django.utils.translation import gettext_lazy as _

from rhazes_test.logger import get_logging_configuration

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rhazes_test.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = "none"

DEBUG = True
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
DATETIME_INPUT_FORMATS += (DATETIME_FORMAT,)

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1',
)

RHAZES_PACKAGES = [
    "app1.services"
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    "DATETIME_FORMAT": DATETIME_FORMAT,
}

AUTHENTICATION_BACKENDS = []

ROOT_URLCONF = "rhazes_test.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rhazes_test.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
USE_I18N = True
LANGUAGES = (
    ("de-at", _("Austria")),
    ("de-de", _("Germany")),
    ("en", _("Great Britain")),
)

LANGUAGE_CODE = "en-us"
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)
LANGUAGE_NAMES = (
    ("de-de", _("German")),
    ("de", _("German")),
    ("en", _("English-UK")),
)

# static i18n package settings
STATICI18N_DOMAIN = "djangojs"
STATICI18N_ROOT = os.path.join(BASE_DIR, "rhazes_test", "static")
STATICI18N_OUTPUT_DIR = "jsi18n"
STATICI18N_FILENAME_FUNCTION = "rhazes_test.utils.static_i18n_filename"

USE_L10N = True
USE_TZ = True
TIME_ZONE = "UTC"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'locale/static')
]

# Media Folder Settings
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DATETIME_FORMAT_READABLE = "%d.%m.%Y %H:%M:%S"



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ORIGIN_WHITELIST = ["*"]


# Logging
LOGGING = get_logging_configuration()
