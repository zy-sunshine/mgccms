# Django settings for MagicLinux project.
import os
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
FILE_CHARSET = 'gbk'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(ROOT_PATH, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '719u8z@p0x1ckx(-u&t&bg@m1@t3at65di94+d!+pl2q%i+4#z'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'mgccms.context_processors.common',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'magicsite.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH,'templates/diy_sample/'),
    os.path.join(ROOT_PATH,'templates/default/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.comments',
    
    'mgccms',
    'mgcindex',
    'mgcnews',
    'mgcprojects',
    'attachments',
    #'mgcguide',
    #'mgcproject',
    #'mgchistory',
    'tinymce',
    'tagging',
)

SITE_CONFIG = {'title': u'MagicLinux',
        'index_url': u'/',
        'news_url': u'/news/',
        'guide_url': u'/guides/',
        'projects_url': u'/projects/',
        'history_url': u'/history/',
        'search_url': u'/search/',
        'accounts_url': u'/accounts/',
        'navi_focous': ' class="current_page_item"',
        'End': '',
        }

TINYMCE_SPELLCHECKER = True
TINYMCE_JS_URL = os.path.join(MEDIA_URL, "tiny_mce/tiny_mce_src.js")
TINYMCE_COMPRESSOR = False

# Check to see if django-filebrowser is installed
try:
    import filebrowser
    INSTALLED_APPS += ('filebrowser',)
    FILEBROWSER_URL_FILEBROWSER_MEDIA = MEDIA_URL + 'filebrowser/'
    TINYMCE_FILEBROWSER = True
except ImportError:
    pass

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "spellchecker",
    'theme_advanced_buttons3_add': "|,spellchecker",
}
