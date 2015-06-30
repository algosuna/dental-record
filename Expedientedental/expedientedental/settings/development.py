import os
from django.core.exceptions import ImproperlyConfigured

from .base import *


def get_env_variable(var_name):
    ''' Get the environment variable or return exception. '''
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Configura la variable de entorno {}'.format(var_name)
        raise ImproperlyConfigured(error_msg)

DEBUG = True

TEMPLATE_DEBUG = DEBUG

THUMBNAIL_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dentaldb',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SECRET_KEY = get_env_variable('SECRET_KEY')
