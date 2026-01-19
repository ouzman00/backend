from pathlib import Path
import os

# ------------------ GDAL / GEOS (OSGeo4W) ------------------
os.environ["OSGEO4W_ROOT"] = r"C:\OSGeo4W"
os.environ["GDAL_DATA"] = r"C:\OSGeo4W\share\gdal"
os.environ["PROJ_LIB"] = r"C:\OSGeo4W\share\proj"
os.environ["PATH"] = r"C:\OSGeo4W\bin;" + os.environ["PATH"]

GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal308.dll"
GEOS_LIBRARY_PATH = r"C:\OSGeo4W\bin\geos_c.dll"

# ------------------ BASE ------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-..."
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# ------------------ APPS ------------------
INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "rest_framework",
    "rest_framework_gis",
    "maps",
]

# ------------------ MIDDLEWARE ------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ------------------ URLS / WSGI ------------------
ROOT_URLCONF = "mybackend.urls"
WSGI_APPLICATION = "mybackend.wsgi.application"

# ------------------ TEMPLATES ------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ------------------ DATABASE ------------------
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "poweend",
        "USER": "poweend",
        "PASSWORD": "Poweend26",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# ------------------ I18N ------------------
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ------------------ STATIC (✅ manquait ici) ------------------
STATIC_URL = "static/"

# (optionnel en dev)
# STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------ CORS ------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ALLOW_ALL_ORIGINS = False
