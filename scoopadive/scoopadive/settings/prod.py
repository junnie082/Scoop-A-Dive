from .base import *

ALLOWED_HOSTS = ['3.36.81.50', 'scoopadive.com']
STATIC_ROOT = str(BASE_DIR / 'main/static/')

print("STATIC_ROOT: " + STATIC_ROOT)
STATICFILES_DIRS = []
DEBUG = True
