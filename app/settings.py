import os


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

RELOADER = True

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')


LOGGING_CONFIG = {}
