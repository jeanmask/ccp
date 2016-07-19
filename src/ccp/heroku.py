import os

import dj_database_url

from .settings import *

DEBUG = TEMPLATE_DEBUG = bool(os.environ.get('ENVIRONMENT') != 'production')

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
