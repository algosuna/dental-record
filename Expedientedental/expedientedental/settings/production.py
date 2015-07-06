import json
from django.core.exceptions import ImproperlyConfigured
from .base import *

with open(BASE_DIR.child('cfg.json')) as cfg:
    config = json.loads(cfg.read())


def get_config(setting, config=config):
    ''' Get configuration variables or return detailed exception. '''
    try:
        return config[setting]
    except KeyError:
        error_msg = 'Configura la variable de entorno {0}'.format(setting)
        raise ImproperlyConfigured(error_msg)

DEBUG = False

ALLOWED_HOSTS = []

SECRET_KEY = get_config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_config('DATABASE')['NAME'],
        'USER': get_config('DATABASE')['USER'],
        'PASSWORD': get_config('DATABASE')['PASSWORD'],
        'HOST': get_config('DATABASE')['HOST'],
        'PORT': '',
    }
}

# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = BASE_DIR.child('static')

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_AGE = 60 * 60 * 8

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR.child('logs/debug.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
