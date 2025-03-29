AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

import datetime

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=2),
    'REFRESH_TOKEN_REISSUE_WINDOW': datetime.timedelta(seconds=60),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'TOKEN_OBTAIN_SERIALIZER': 'common.serializers.auth.TokenObtainPairSerializer',
    'TOKEN_REFRESH_SERIALIZER': 'common.serializers.auth.CustomTokenRefreshSerializer',
    'UPDATE_LAST_LOGIN': True,
    "USER_AUTHENTICATION_RULE": "common.permissions.default_user_authentication_rule",
}