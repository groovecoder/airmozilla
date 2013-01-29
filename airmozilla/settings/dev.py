# This is an example settings/local.py file.
# These settings overrides what's in settings/base.py

from . import base

# to be able to run unit tests enable django_nose
INSTALLED_APPS = base.INSTALLED_APPS + ['django_nose']

# To extend any settings from settings/base.py here's an example:
INSTALLED_APPS = base.INSTALLED_APPS + ['debug_toolbar']
MIDDLEWARE_CLASSES = base.MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INTERNAL_IPS = ('127.0.0.1',)
JINGO_EXCLUDE_APPS = base.JINGO_EXCLUDE_APPS + [
    'debug_toolbar',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'airmozilla',
        'USER': 'root',
        'PASSWORD': 'r00t',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET storage_engine=InnoDB',
            'charset' : 'utf8',
            'use_unicode' : True,
        },
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_general_ci',
    },
    # 'slave': {
    #     ...
    # },
}

# Uncomment this and set to all slave DBs in use on the site.
# SLAVE_DATABASES = ['slave']

# Recipients of traceback emails and other notifications.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True

# If you intend to run on something like http://127.0.0.1:8000 then
# set this False so cookies can be set with HTTP
SESSION_COOKIE_SECURE = False

# By default, BrowserID expects your app to use http://127.0.0.1:8000
# Uncomment the following line if you prefer to access your app via localhost
#SITE_URL = 'http://localhost:8000'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher'
)

# Make this unique, and don't share it with anybody.  It cannot be blank.
SECRET_KEY = '41rm0z1ll4'

# Uncomment these to activate and customize Celery:
# CELERY_ALWAYS_EAGER = False  # required to activate celeryd
# BROKER_HOST = 'localhost'
# BROKER_PORT = 5672
# BROKER_USER = 'playdoh'
# BROKER_PASSWORD = 'playdoh'
# BROKER_VHOST = 'playdoh'
# CELERY_RESULT_BACKEND = 'amqp'

## Log settings

# SYSLOG_TAG = "http_app_playdoh"  # Make this unique to your project.
# LOGGING = dict(loggers=dict(playdoh={'level': logging.DEBUG}))

# Common Event Format logging parameters
#CEF_PRODUCT = 'Playdoh'
#CEF_VENDOR = 'Mozilla'


# Caching - use local memory
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': 'airmoz',
        'TIMEOUT': 6 * 60 * 60,
        'LOCATION': ''
    }
}

EMAIL_FROM_ADDRESS = 'airmozilla-ops@mozilla.com'

# for debugging/development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# These need to be filled in to able to use Vid.ly's secure tokens
# See https://bugzilla.mozilla.org/show_bug.cgi?id=798572#c2
VIDLY_USER_ID = ''
VIDLY_USER_KEY = ''
