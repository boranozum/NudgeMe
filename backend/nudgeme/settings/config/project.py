from os import path

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

AUTH_USER_MODEL = "accounts.User"

ROOT_URLCONF = 'nudgeme.urls'

WSGI_APPLICATION = 'nudgeme.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True

SETTINGS_PATH = path.dirname(path.abspath(__file__))

LOCALE_PATHS = (
    path.join(SETTINGS_PATH, '../locale'),
    path.join(SETTINGS_PATH, '../locale_extra'),
)
