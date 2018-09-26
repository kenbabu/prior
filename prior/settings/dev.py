from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# print("SECRET KEY {}".format(SECRET_KEY))
config.DATABASE_URL = 'bolt://neo4j:{}@localhost:7687'.format(neopassword)
