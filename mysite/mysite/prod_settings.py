import os

DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

# DB設定
import dj_database_url

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
db_from_env = dj_database_url.config()
DATABASES = {
    'default': dj_database_url.config()
}
ALLOWED_HOSTS = ['*']
