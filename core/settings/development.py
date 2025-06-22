"""
Development settings for core project.
"""

from .base import *
from decouple import config

DEBUG = config('DEBUG', default=True, cast=bool)
SECRET_KEY = config('SECRET_KEY', default='your-secret-key-goes-here-in-development')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@kynyeacademy.com')

# CORS settings
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', 
                            default='http://localhost:3000,http://127.0.0.1:3000',
                            cast=Csv())

# Override Djoser settings for development
DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': False,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': False,
    'SEND_CONFIRMATION_EMAIL': False,
    'SEND_ACTIVATION_EMAIL': False,  # This will disable activation email
    'SERIALIZERS': {
        'user_create': 'apps.accounts.serializers.UserCreateSerializer',
        'user': 'apps.accounts.serializers.UserSerializer',
        'current_user': 'apps.accounts.serializers.UserSerializer',
    },
}
