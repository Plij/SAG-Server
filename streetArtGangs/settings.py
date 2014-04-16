"""
Django settings for streetArtGangs project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'file': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',
			'filename': 'streetArtGangs/debug.log',
		},
		'console':{
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
		},
	},
	'loggers': {
		'django.request': {
			'handlers': ['file', 'console'],
			'level': 'DEBUG',
			'propagate': True,
		},
	},
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n^@orv@q9_g=!t2)f+_=q@t!otx8uam&%a304v2p9(%=tc^-nw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'server',
    'django_extensions',
    'debug_toolbar',	
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'streetArtGangs.urls'

WSGI_APPLICATION = 'streetArtGangs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {

    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': 'graffiti',
    # }

   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'graffiti',
       'USER': 'gangAdmin',
       'PASSWORD': 'streetArtGangs',
       'HOST': '127.0.0.1',
       'PORT': '3306',
   }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Custom User prifile
AUTH_PROFILE_MODULE='server.UserProfile'

#CORS
CORS_ORIGIN_ALLOW_ALL = True
