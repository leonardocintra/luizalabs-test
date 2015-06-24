import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ.get('DEBUG', False)

DATABASE = {
    'ENGINE': os.environ['DB_ENGINE'],
    'NAME': os.environ['DB_NAME'],
    'USER': os.environ['DB_USER'],
    'PASSWORD': os.environ['DB_PASSWORD'],
    'HOST': os.environ['DB_HOST'],
    'PORT': os.environ['DB_PORT']
}

TEMPLATE_PATH = os.path.join(BASE_DIR, 'views')

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')


FACEBOOK_GRAPH = {
    'access_token': os.environ['FB_ACCESS_TOKEN']
}


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
