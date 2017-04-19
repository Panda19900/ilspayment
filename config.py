# Base off Google config file

import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'secret'


# There are three different ways to store the data in the application.
# Choose 'datastore', 'cloudsql', or 'mongodb'.
DATA_BACKEND = 'datastore'

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'lims-payment'

# CloudSQL & SQLAlchemy configuration
CLOUDSQL_USER = 'root'
CLOUDSQL_PASSWORD = 'your-cloudsql-password'
CLOUDSQL_DATABASE = 'tests'
# Set this value to the Cloud SQL connection name, e.g.
#   "project:region:cloudsql-instance".
# You must also update the value in app.yaml.
CLOUDSQL_CONNECTION_NAME = 'your-cloudsql-connection-name'

# The CloudSQL proxy is used locally to connect to the cloudsql instance.
# To start the proxy, use:
#
#   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306

#MySQL instance for testing.
LOCAL_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{user}:{password}@127.0.0.1:3306/{database}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
        database=CLOUDSQL_DATABASE)

# When running on App Engine a unix socket is used to connect to the cloudsql
# instance.
LIVE_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{user}:{password}@localhost/{database}'
    '?unix_socket=/cloudsql/{connection_name}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
        database=CLOUDSQL_DATABASE, connection_name=CLOUDSQL_CONNECTION_NAME)

if os.environ.get('GAE_INSTANCE'):
    SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
else:
    SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI

# Mongo configuration.
MONGO_URI = 'mongodb://user:password@host:27017/database'

# Google Cloud Storage and upload settings.
CLOUD_STORAGE_BUCKET = 'your-bucket-name'
MAX_CONTENT_LENGTH = 8 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# OAuth2 configuration.
GOOGLE_OAUTH2_CLIENT_ID = \
    ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''
