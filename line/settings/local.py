DEBUG = True
TEMPLATE_DEBUG = DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cf9@6x8&&m9qo-ogk%=c-)uk@u8vk*3_$7c4ysf=r-16)7)@0y'
  
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'line',
    }
}

ALLOWED_HOSTS = [
    'localhost',
]

# S3 config
AWS_STORAGE_BUCKET_NAME = 'line-jack-reuter'
AWS_ACCESS_KEY_ID = 'AKIAJPLAOMVRPHERXZKA'
AWS_SECRET_ACCESS_KEY = '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'

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
