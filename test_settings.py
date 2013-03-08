from settings import *

INSTALLED_APPS = tuple([app for app in INSTALLED_APPS if app != "south"])
INSTALLED_APPS = INSTALLED_APPS + (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Usamos una BD sqlite3 en memoria para agilizar la velocidad de los tests. Innecesario si la BD del proyecto ya es sqlite.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'TEST_NAME': ':memory:',
    }
}

