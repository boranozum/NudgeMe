from nudgeme.settings.vars import env

LANGUAGE_CODE = env('LANGUAGE_CODE')

TIME_ZONE = env('TIME_ZONE')

USE_I18N =  True if env('USE_I18N')=="True" else False

USE_TZ = True if env('USE_TZ')=="True" else False
