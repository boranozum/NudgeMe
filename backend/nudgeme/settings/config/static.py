import os

from nudgeme.settings.vars import BASE_DIR

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []
