# Deployment Guide for Django Project on Render

This document provides a step-by-step guide on how to deploy your Django project to Render.

---

## 1. Install Required Packages

### Install Gunicorn

Gunicorn is a WSGI HTTP server required for serving Django applications in production.

```bash
pip install gunicorn
```

### Install Whitenoise

Whitenoise is used to serve static files in production.

```bash
pip install whitenoise
```

### Update `requirements.txt`

After installing the required packages, update your `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

---

## 2. Update `settings.py` for Production

### Static Files Configuration

Add the following settings to handle static files in production:

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Middleware Configuration

Add `WhitenoiseMiddleware` to the `MIDDLEWARE` list, just after `SecurityMiddleware`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### Allowed Hosts

Add your Render domain to the `ALLOWED_HOSTS` list:

```python
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'your-app-name.onrender.com']
```

---

## 3. Prepare the Project for Deployment

### Run `collectstatic`

Run the following command to collect all static files into the `STATIC_ROOT` directory:

```bash
python manage.py collectstatic --noinput
```

---

## 4. Push Your Project to GitHub

Render requires your project to be hosted on a Git repository like GitHub.

### Steps to Push to GitHub

1. Initialize Git in your project directory (if not already done):
   ```bash
   git init
   ```
2. Add all files to the Git staging area:
   ```bash
   git add .
   ```
3. Commit the changes:
   ```bash
   git commit -m "Initial commit for Render deployment"
   ```
4. Create a repository on GitHub and link it:
   ```bash
   git remote add origin https://github.com/your-username/your-repository.git
   git branch -M main
   git push -u origin main
   ```

---

## 5. Deploy to Render

### Create a New Web Service

1. Log in to [Render](https://render.com/).
2. Click **New** > **Web Service**.
3. Connect your GitHub repository and select your Django project.

### Configure the Web Service

- **Name**: Enter a name for your app.
- **Environment**: Select **Python**.
- **Build Command**:
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput
  ```
- **Start Command**:
  ```bash
  gunicorn calculator.wsgi
  ```
  Replace `calculator` with the name of your Django project folder (the one containing `settings.py`).

---

## 6. Add Environment Variables

1. Go to your Render Web Service dashboard.
2. Add the following environment variables:
   - `SECRET_KEY`: Your Django secret key.
   - `DEBUG`: Set to `False` for production.
   - `ALLOWED_HOSTS`: Add your Render domain (e.g., `your-app-name.onrender.com`).

---

## 7. Verify the Deployment

Once the deployment is complete:

1. Visit your app's URL (e.g., `https://your-app-name.onrender.com`).
2. Verify that the app is working correctly.
3. Check the browser's developer tools to ensure static files (e.g., CSS, JavaScript) are being served correctly.

---

## 8. Debugging Common Issues

### Static Files Not Loading

- Ensure `collectstatic` ran successfully during deployment.
- Verify that the `STATIC_URL` and `STATIC_ROOT` settings are correct.
- Check if `WhitenoiseMiddleware` is added to the `MIDDLEWARE` list.

### DisallowedHost Error

- Ensure your Render domain is added to the `ALLOWED_HOSTS` list in `settings.py`.

---

## 9. Example `settings.py` for Production

Here’s an example `settings.py` file configured for production:

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_calculator',  # Your app
]

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

ROOT_URLCONF = 'calculator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'calculator.wsgi.application'

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

---
