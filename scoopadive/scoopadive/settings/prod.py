from .base import *

ALLOWED_HOSTS = ['52.78.240.94']
STATIC_ROOT = str(BASE_DIR / 'static/')

print("STATIC_ROOT: " + STATIC_ROOT)
STATICFILES_DIRS = []
DEBUG = True
