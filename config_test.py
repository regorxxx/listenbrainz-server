DEBUG = False  # set to False in production mode

SECRET_KEY = "yer mom"


# DATABASES

# Primary database
SQLALCHEMY_DATABASE_URI = "postgresql://listenbrainz:listenbrainz@db_test:5432/listenbrainz"
MESSYBRAINZ_SQLALCHEMY_DATABASE_URI = "postgresql://messybrainz:messybrainz@db_test:5432/messybrainz"

POSTGRES_ADMIN_URI="postgresql://postgres@db_test/template1"


# Other postgres configuration options
# Oldest listens which can be stored in the database, in days.
MAX_POSTGRES_LISTEN_HISTORY = "-1"
# Log Postgres queries if they execeed this time, in milliseconds.
PG_QUERY_TIMEOUT = "3000"
# Set to True to enable 'synchronous_commit' for Postgres. Default: False
PG_ASYNC_LISTEN_COMMIT = False
# The name of a postgres user who has superuser privileges. Your local user should
# be able to connect to the database with this user.
PG_SUPER_USER = "postgres"


# Redis
REDIS_HOST = "redis_test"

# Influx DB (main listen store)
INFLUX_HOST    = "influx_test"
INFLUX_PORT    = 8086
INFLUX_DB_NAME  = "listenbrainz"


# MusicBrainz OAuth
MUSICBRAINZ_CLIENT_ID = "CLIENT_ID"
MUSICBRAINZ_CLIENT_SECRET = "CLIENT_SECRET"

# Lastfm API key
LASTFM_API_KEY = "USE_LASTFM_API_KEY"

# BigQuery support
# Enable/disable support. If enabled, the Application Credentials must reside in 
# bigquery-credentials.json in the top level directory.
WRITE_TO_BIGQUERY = False


# Max time in seconds after which the playing_now stream will expire.
PLAYING_NOW_MAX_DURATION = 10 * 60

# LOGGING

#LOG_FILE_ENABLED = True
#LOG_FILE = "./listenbrainz.log"

#LOG_EMAIL_ENABLED = True
#LOG_EMAIL_TOPIC = "ListenBrainz Webserver Failure"
#LOG_EMAIL_RECIPIENTS = []  # List of email addresses (strings)

#LOG_SENTRY_ENABLED = True
#SENTRY_DSN = ""


# MISCELLANEOUS

# Set to True if Less should be compiled in browser. Set to False if styling is pre-compiled.
COMPILE_LESS = True

# MAX file size to be allowed for the lastfm-backup import, default is infinite
# Size is in bytes
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# Specify the upload folder where all the lastfm-backup will be stored
# The path must be absolute path
UPLOAD_FOLDER = "/tmp/lastfm-backup-upload"
