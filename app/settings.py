class Config(object):
    PORT = 3001
    HOST = '0.0.0.0'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/test.db'


class TestingConfig(Config):
    TESTING = True
