from settings import *

INSTALLED_APPS = tuple([app for app in INSTALLED_APPS if app != "south"])
INSTALLED_APPS = INSTALLED_APPS + (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

