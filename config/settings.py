DEBUG = True
SECRET_KEY = '123456789'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROOT_URLCONF = 'config.urls'

MIDDLEWARE = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_migration_error',
        'HOST': 'localhost',
        'USER': 'django',
        'PASSWORD': 'password',
    }
}

INSTALLED_APPS = [
        'polls',
    ]
