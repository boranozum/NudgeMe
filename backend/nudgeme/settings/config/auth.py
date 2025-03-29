AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

import datetime

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(days=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': datetime.timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': datetime.timedelta(days=30),
    'TOKEN_OBTAIN_SERIALIZER': 'accounts.serializers.auth.TokenObtainCustomSerializer',
    'UPDATE_LAST_LOGIN': True,
}