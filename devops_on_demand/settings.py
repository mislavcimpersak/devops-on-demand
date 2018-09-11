import os
import environ
from configurations import Configuration


# Django-Environ instance that will parse the enviroment variables
ENV = environ.Env()

BASE_DIR = environ.Path(__file__) - 2
ENV.read_env(str(BASE_DIR.path(".env")))


class BaseConfig(Configuration):
    """Base Django Configuration class with values repeated among all the environments."""

    DEBUG = False

    ALLOWED_HOSTS = []

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = ENV.str("SECRET_KEY")

    STATIC_DIR = str(BASE_DIR.path("static/"))

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # 3rd party
        "rest_framework",
        # project apps
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

    ROOT_URLCONF = "devops_on_demand.urls"

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
                ]
            },
        }
    ]

    WSGI_APPLICATION = "devops_on_demand.wsgi.application"

    DATABASES = {
        "default": ENV.db(
            default="sqlite:///db.sqlite3"
        )  # will read the DATABASE_URL env var
    }

    # Password validation
    # https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/2.1/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.1/howto/static-files/

    STATIC_URL = "/static/"


class DevConfig(BaseConfig):
    """Django Configuration class with specific for the local environment."""

    DEBUG = True

    INSTALLED_APPS = BaseConfig.INSTALLED_APPS + ["django_extensions"]


class ProdConfig(BaseConfig):
    """Django Configuration class with specific for the production environment."""

    pass
