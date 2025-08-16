from environ import Env
from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Initialize environment variables
env = Env()
Env.read_env()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Security settings
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # Required for Heroku

# Secret Key & Debug Mode
SECRET_KEY = env("DJANGO_SECRET_KEY", default="No Secret Key Found")
DEBUG = env.bool("DJANGO_DEBUG", default=False)

# ✅ Allowed Hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[
    "localhost",
    "127.0.0.1",
    "art-moving-buisness-0a734245a61f.herokuapp.com",
    "ejartmover.net",
    "www.ejartmover.net"
])

# ✅ Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party packages - CLOUDINARY MUST BE BEFORE CUSTOM APPS
    'cloudinary_storage',
    'cloudinary',
    'crispy_forms',
    'crispy_bootstrap5',
    'import_export',

    # Custom apps
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    'workorders',
    'clients',
    'invoices',
    "calendar_app",
]

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ URL Configuration
ROOT_URLCONF = 'django_project.urls'

# ✅ Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Include custom templates
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

# ✅ WSGI Application
WSGI_APPLICATION = 'django_project.wsgi.application'

# ✅ Database Configuration
DATABASES = {
    "default": env.db_url("DATABASE_URL")
}

# ✅ Authentication
AUTH_USER_MODEL = 'accounts.CustomUser'

# ✅ Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static Files Configuration
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ Media Files Configuration
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ✅ Cloudinary Configuration
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME', default=''),
    'API_KEY': env('CLOUDINARY_API_KEY', default=''),
    'API_SECRET': env('CLOUDINARY_API_SECRET', default=''),
}

# Configure cloudinary
cloudinary.config(
    cloud_name=env('CLOUDINARY_CLOUD_NAME', default=''),
    api_key=env('CLOUDINARY_API_KEY', default=''),
    api_secret=env('CLOUDINARY_API_SECRET', default=''),
    secure=True
)

# ✅ Storage Configuration - Environment Based
if not DEBUG:
    # Production: Use Cloudinary and WhiteNoise
    STORAGES = {
        "default": {
            "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
    
    # Validate Cloudinary credentials in production
    cloudinary_vars = [
        env('CLOUDINARY_CLOUD_NAME', default=''),
        env('CLOUDINARY_API_KEY', default=''),
        env('CLOUDINARY_API_SECRET', default='')
    ]
    
    if not all(cloudinary_vars):
        print("WARNING: Cloudinary credentials not fully configured")
        print(f"CLOUD_NAME: {'✓' if cloudinary_vars[0] else '✗'}")
        print(f"API_KEY: {'✓' if cloudinary_vars[1] else '✗'}")
        print(f"API_SECRET: {'✓' if cloudinary_vars[2] else '✗'}")
        
    # WhiteNoise configuration for production
    WHITENOISE_USE_FINDERS = True
    WHITENOISE_AUTOREFRESH = False
    WHITENOISE_MAX_AGE = 31536000  # 1 year
    
else:
    # Development: Use local storage
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
    
    # Development WhiteNoise settings
    WHITENOISE_USE_FINDERS = True
    WHITENOISE_AUTOREFRESH = True

# ✅ Static Files Finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# ✅ Default Primary Key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ✅ Login & Logout
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = "/"  

# ✅ Import/Export
IMPORT_EXPORT_USE_TRANSACTIONS = True

# ✅ Security Settings for Production
if not DEBUG:
    SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
    SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000)  # 30 days
    SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
    SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
    SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)
    CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    
    # ✅ Logging Configuration for Production
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': '/tmp/django_errors.log',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'file'],
                'level': 'INFO',
                'propagate': True,
            },
            'django.request': {
                'handlers': ['console', 'file'],
                'level': 'ERROR',
                'propagate': False,
            },
            'cloudinary': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': True,
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
    
else:
    # Development security settings (less strict)
    SECURE_SSL_REDIRECT = False
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    
    # ✅ Development Logging (simpler)
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': True,
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }

# ✅ Debug Information (helpful for troubleshooting)
if DEBUG:
    print(f"🐛 DEBUG MODE: {DEBUG}")
    print(f"📁 STATIC_ROOT: {STATIC_ROOT}")
    print(f"📁 MEDIA_ROOT: {MEDIA_ROOT}")
    print(f"☁️  CLOUDINARY_CLOUD_NAME: {env('CLOUDINARY_CLOUD_NAME', default='NOT SET')}")
    print(f"🗄️  DATABASE_URL exists: {bool(env('DATABASE_URL', default=''))}")
    print(f"🏠 ALLOWED_HOSTS: {ALLOWED_HOSTS}")
else:
    print(f"🚀 PRODUCTION MODE: DEBUG={DEBUG}")
    print(f"☁️  Cloudinary configured: {bool(env('CLOUDINARY_CLOUD_NAME', default=''))}")
    print(f"🏠 ALLOWED_HOSTS: {len(ALLOWED_HOSTS)} hosts configured")

# ✅ Error Pages Configuration
# Django will look for 400.html, 403.html, 404.html, 500.html in your templates directory