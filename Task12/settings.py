"""
Django settings for task12 project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)i2zhl2kxtfhkho079hbhg-p$u(ve%r==+!4x#4i2hf#b@_8mj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'djangogram01.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'debug_toolbar',
    'whitenoise.runserver_nostatic',
    'taggit',
    'social_django',

    'djangogram.apps.DjangogramConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Task12.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'Task12.wsgi.application'

db_config = dj_database_url.config(
    default='postgres://wpyindjezdaokr:9a68dcc2286670f88a23d08129f2042e44cf54b2c6db813334fe177fcc06322b@'
            'ec2-52-211-182-159.eu-west-1.compute.amazonaws.com:5432/d8fdehua5pbljp')
db_config['ATOMIC_REQUESTS'] = True

DATABASES = {
    'default': db_config,
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'djangogram',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Task12/static')
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

INTERNAL_IPS = [
    "127.0.0.1",
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dwhehigeg',
    'API_KEY': '271944658343995',
    'API_SECRET': 'kcqyJ-o3SqnfMKTgXOmRiFw59-I'
}

SOCIAL_AUTH_JSONFIELD_ENABLED = True

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '466429154851-dq747907pad6onub56h0nh7edisjcor7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_FACEBOOK_KEY = '5814701555287225'
SOCIAL_AUTH_FACEBOOK_SECRET = '3259bb40ef62dc90445da421b4590b69'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
   'fields': 'id, name, email, age_range'
}
# SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

SOCIAL_AUTH_GITHUB_KEY = 'ae94db50ea95e3ba945c'
SOCIAL_AUTH_GITHUB_SECRET = '39ab34d40ac7ead52a2c521db38844025cc725c4'
SOCIAL_AUTH_GITHUB_SCOPE = ['read:user', 'user:email']

LOGIN_URL = 'login/google-oauth2/'
# LOGIN_URL = 'login/'
LOGOUT_URL = 'logout/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# def save_profile(backend, user, response, is_new=False, *args, **kwargs):
#     from djangogram.models import Profile
#     if is_new and backend.name == "facebook":
#         # The main part is how to get the profile picture URL and then do what you need to do
#         Profile.objects.filter(user=user).update(
#             imageUrl=f'https://graph.facebook.com/{response["id"]}/picture/?type=large&access_token={response["access_token"]}')

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    # 'social_core.pipeline.social_auth.save_profile',
)
SOCIAL_AUTH_CLEAN_USERNAMES = True


# SOCIAL_AUTH_PIPELINE += ('social_core.pipeline.social_auth.save_profile',)