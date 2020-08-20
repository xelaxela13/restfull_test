SECRET_KEY = 'test_secret_key'
ALLOWED_HOSTS = ['*']
ADMINS = [('Admin', 'dummy@mail.com')]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
    }
}
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGGING = False
