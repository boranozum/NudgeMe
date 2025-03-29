from nudgeme.settings.vars import env

DATABASES = {
    'default': {
        "ENGINE": env('DATABASE_DEFAULT_ENGINE'),
        "NAME": env('DATABASE_DEFAULT_NAME'),
        "USER": env('DATABASE_DEFAULT_USER'),
        "PASSWORD": env('DATABASE_DEFAULT_PASSWORD'),
        "HOST": env('DATABASE_DEFAULT_HOST'),
        "PORT": int(env('DATABASE_DEFAULT_PORT')),
        "CONN_HEALTH_CHECKS": True,
        "OPTIONS": {
            "options": env('DATABASE_DEFAULT_OPTIONS')
        },
    },
}
