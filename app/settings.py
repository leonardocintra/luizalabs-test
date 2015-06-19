import os


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

RELOADER = True

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '../luizalabs.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'luizalabs': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
