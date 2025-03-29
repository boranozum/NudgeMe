from nudgeme.settings.vars import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if env('DEBUG')=="True" else False
