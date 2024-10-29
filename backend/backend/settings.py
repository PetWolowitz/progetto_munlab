import os
from pathlib import Path

# Percorso base del progetto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chiave segreta (non condividere mai questa chiave)
SECRET_KEY = 'la-tua-chiave-segreta-qui'

# Modalità debug
DEBUG = True

ALLOWED_HOSTS = []

# Applicazioni installate
INSTALLED_APPS = [
    # App predefinite di Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # App di terze parti
    'rest_framework',
    'corsheaders',

    # La tua app
    'prenotazioni',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Deve essere il primo
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL di root
ROOT_URLCONF = 'backend.urls'

# Template
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Aggiungi qui le directory dei template se necessario
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Processori di contesto predefiniti
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # Validatori predefiniti
]

# Internazionalizzazione
LANGUAGE_CODE = 'it-it'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# URL statici
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Configurazione CORS
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

# Configurazione Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}

# Altre configurazioni...
