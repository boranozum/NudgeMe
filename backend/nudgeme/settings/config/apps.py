if "INSTALLED_APPS" not in locals():
    INSTALLED_APPS = []

# noinspection PyUnboundLocalVariable
PROJECT_APPS = [
    "accounts",
    "events",
    # 3rd Party Apps
    'corsheaders',
    'drf_spectacular',
]

INSTALLED_APPS += PROJECT_APPS

# Channels
ASGI_APPLICATION = 'nudgeme.asgi.application'

