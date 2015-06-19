import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))


TEMPLATE_PATH = os.path.join(BASE_DIR, 'views')

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
