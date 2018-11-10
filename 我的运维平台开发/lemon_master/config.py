class Config(object):
    # Statement for enabling the development environment
    DEBUG = True

    # Define the application directory
    import os
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Define the SQLALCHEMY  database - we are working with
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:950428@127.0.0.1/Lemon_GO'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED     = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    # mysql db
    mysql_server = '127.0.0.1'
    mysql_username = 'root'
    mysql_password = '950428'
    mysql_port = 3306
    mysql_db = 'Lemon_GO'

    # python 3 path
    python3_path = '/opt/python-3.5.1/bin/python3'

    # python 2 path
    python2_path = '/usr/bin/python'


