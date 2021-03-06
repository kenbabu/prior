from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# print("SECRET KEY {}".format(SECRET_KEY))

# Export to raw json
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

config.AUTO_INSTALL_LABELS = True
config.DATABASE_URL = 'bolt://neo4j:{}@localhost:7687'.format(neopassword)
