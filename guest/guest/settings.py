"""
Django settings for guest project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v3a%0r9ravr$@eb988i1ifj*c_3@ft-8*%^yw4-0y@2#8j+2h$'

# SECURITY WARNING: don't run with debug turned on in production! 上线的时候要改为False
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # 后台管理
    'django.contrib.auth',   # 认证
    'django.contrib.contenttypes',
    'django.contrib.sessions',  #用来存session的模块（执行python manage.py migrate即可），里面已经设计好库表，对应的db在下面的database
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sign',
    'bootstrap3',

]

# 中间件，当Django处理一个 Request 的过程是首先通过中间件，然后再通过默认的 URL 方式进行的。
# 我们可以在 Middleware 这个地方把所有Request 拦截住，用我们自己的方式完成处理以后直接返回 Response。
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'guest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  #不使用默认的模板，需要在这里指定自定义的模板路径，比如'DIRS': ["d://aa","e//b//c"]
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

WSGI_APPLICATION = 'guest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
'''
# sqlite3 config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}
'''

# mysql config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'my.cnf'),
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'    # 设置简体中文，zh-Hant是繁体中文

# TIME_ZONE = 'UTC'    # 时区
TIME_ZONE = 'Asia/Shanghai'        # 设置为中国的时区

USE_I18N = True

USE_L10N = True

USE_TZ = False    # 设置为False，要不然数据库时间和当前时间不一致


# Static files (CSS, JavaScript, Images，图片、视频、音频)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
