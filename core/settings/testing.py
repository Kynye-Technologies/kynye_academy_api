"""
Testing settings for core project.
"""

from .base import *

DEBUG = False
SECRET_KEY = 'test-secret-key'
ALLOWED_HOSTS = ['testserver']

# Critical settings that need to be explicitly set for tests
AUTH_USER_MODEL = 'accounts.User'  # Ensure this is set for tests

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Make password hashing faster for tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable CORS in testing
CORS_ALLOWED_ORIGINS = []
