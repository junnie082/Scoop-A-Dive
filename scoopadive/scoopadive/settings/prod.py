from .base import *

ALLOWED_HOSTS = ['3.36.81.50']
STATIC_ROOT = BASE_DIR / 'static/'
print("STATIC_ROOT: " + STATIC_ROOT)
STATICFILES_DIRS = []
DEBUG = False