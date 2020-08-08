from .common import *
import dj_database_url
 
DEBUG = False
 
ALLOWED_HOSTS = ['.herokuapp.com']
 
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'c1',
        'USER': 'roshan98',
        'PASSWORD': 'Roshan98',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
 
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)