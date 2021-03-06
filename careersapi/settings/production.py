
import  os
BASE_DIR     = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
     'default': {                 # Set to empty string for default. Not used with sqlite3.
    }
}
# pg_dump -U nzmewqyrvjyhpl -h ec2-107-22-173-160.compute-1.amazonaws.com dcoimmfelmkfbc > winda_backup

# Update database configuration with $DATABASE_URL.
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

#careersadmin
# Extra places for collectstatic to find static files.
EMAIL_USE_SSL = True
EMAIL_HOST="smtp.webfaction.com"
EMAIL_HOST_USER="micha"
EMAIL_HOST_PASSWORD=""
EMAIL_PORT = 465


import sys
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase'
    }

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, '../../templates'),

)
CORS_ORIGIN_ALLOW_ALL=True

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'