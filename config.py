import os


class Config(object):
    DEBUG = False
    TESTING = False

    API_URL = 'https://api.boilerplate.com'

    # Flask-Mail configuration
    MAIL_SERVER = 'none'#amazon ses example: email-smtp.us-west-2.amazonaws.com
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'user'
    MAIL_PASSWORD = 'pass'
    MAIL_DEFAULT_SENDER = 'no-reply@us.com'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_USER = 'a_user'
    DATABASE_PASSWORD = 'a_password'
    DATABASE_HOST = '172.18.0.1'
    DATABASE_PORT = '3306'
    DATABASE_NAME = 'test'
    DATABASE_URI = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    API_URL = 'localhost'


class TestingConfig(Config):
    TESTING = True
    DATABASE_USER = 'a_user'
    DATABASE_PASSWORD = 'a_password'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = '5432'
    DATABASE_NAME = 'test'
    DATABASE_URI = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    API_URL = 'localhost'
