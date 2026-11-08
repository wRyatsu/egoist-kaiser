"""
Configurações do projeto Django — Sazonalizei (Sistema Moderno de Gestão PDV).

Este projeto liga os templates HTML já existentes em /templates ao backend
Python puro localizado em /br/com/pdv/src (InventoryManager, PaymentManager).
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ATENÇÃO: troque essa chave antes de colocar em produção real.
SECRET_KEY = 'django-insecure-troque-esta-chave-antes-de-ir-para-producao-sazonalizei'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Não usamos o ORM do Django — o backend próprio (BancoDB) já cuida do
# SQLite (databaseSazonalizei.db) usado pelo InventoryManager/PaymentManager.
# Mantemos um banco mínimo apenas para as sessões de login funcionarem.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'sessions.sqlite3',
    }
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Manaus'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# Credenciais de acesso simples (sem contrib.auth) — troque em produção.
APP_USUARIO = 'admin'
APP_SENHA = 'admin123'
