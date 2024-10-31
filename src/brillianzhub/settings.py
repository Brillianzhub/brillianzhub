from pathlib import Path
import os
from django.urls import reverse_lazy
import dj_database_url
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Initialize Firebase
# cred = credentials.Certificate(
#     os.path.join(BASE_DIR, 'home/Godyson/brillianzhub/serviceAccountKey.json'))
# firebase_admin.initialize_app(cred)


# Application definition

INSTALLED_APPS = [
    'accounts',

    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'mathfilters',
    'robots',
    'rest_framework',
    'corsheaders',

    'blog',
    'ipray',
    'notifications',
    'community',
    'storages',
    'taggit',
    'ckeditor',

    'consult',
    'policies',
]


AUTH_USER_MODEL = 'accounts.User'

# MAILCHIMP_API_KEY = os.environ.get('MAILCHIMP_API_KEY', '#')
# MAILCHIMP_DATA_CENTER = "us10"
# MAILCHIMP_EMAIL_LIST_ID = os.environ.get("MAILCHIMP_EMAIL_LIST_ID", '#')

SITE_ID = 1


# Sending Email from Django
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'brillianzhub@gmail.com'
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
ACCOUNT_EMAIL_VERIFICATION = 'none'
DEFAULT_FROM_EMAIL = 'Team Brillianz Hub <brillianzhub@gmail.com>'
BASE_URL = 'www.brillianzhub.com'

MANAGERS = (
    ("Team Brillianz Hub", "brillianzhub@gmail.com"),
)

ADMIN = MANAGERS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'brillianzhub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'brillianzhub.wsgi.application'

CORS_ALLOW_ALL_ORIGINS = True


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'Godyson$brillianzhub',
#         'USER': 'Godyson',
#         'PASSWORD': '@administrator',
#         'HOST': 'Godyson.mysql.pythonanywhere-services.com',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# DATABASE_URL = config('DATABASE_URL')

# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# DATABASES['default']['CONN_MAX_AGE'] = 500


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# CKEDITOR_CONFIGS = {
#     'awesome_ckeditor': {
#         'toolbar': 'Basic',
#     },
# }

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'custom_static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "custom_static"),
]

STATIC_ROOT = os.path.join(os.path.dirname(
    BASE_DIR), "static_cdn", "static_root")


MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'custom_media')

MEDIA_ROOT = os.path.join(os.path.dirname(
    BASE_DIR), "static_cdn", "media_root")

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_RESTRICT_BY_USER = True


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'toolbar_Custom',
        'height': 500,

        'toolbar_Custom': [
            ['Styles', 'Format', 'Bold', 'Italic',
             'Underline', 'SpellChecker', 'Undo'],
            ['Link', 'Unlink', 'Anchor', 'Mathjax'],
            ['Image2', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['RemoveFormat', 'Source', 'CodeSnippet', 'Youtube']
        ],

        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'codesnippet',
            'image2',

            'autolink',
            'autoembed',
            'embedsemantic',
            # 'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    },

}


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,  # Set your desired page size
}


LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGIN_URL = reverse_lazy('accounts:login')
LOGOUT_URL = reverse_lazy('home')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOW_CREDENTIALS = True
HOST_SCHEME = "htttp://"
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SECTION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'ipray.backends.EmailAuthBackend',
)
