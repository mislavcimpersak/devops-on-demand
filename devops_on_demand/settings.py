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
        "django.contrib.auth",
        "django.contrib.contenttypes",
        # 3rd party
        "rest_framework",
        # project apps
        "maintenance",
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


class TestConfig(BaseConfig):
    """Django Configuration class with specific settings when running the test suite."""

    pass


class ProdConfig(BaseConfig):
    """Django Configuration class with specific for the production environment."""

    pass
