from .settings_base import *  # noqa: F401,F403
from .settings_base import env_bool


DEBUG = env_bool("DJANGO_DEBUG", True)

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
