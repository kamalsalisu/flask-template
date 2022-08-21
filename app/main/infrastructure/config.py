""" Config sets the configuration depending on the development environment """

import os


class Config:
    """ base class for environment configuration classes """

    SECRET_KEY = os.getenv('SECRET_KEY') or 'my_powerful_secret_key'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ORIGIN = '*'


class DevelopmentConfig(Config):
    """ development environment configuration class """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ContinuousIntegrationConfig(Config):
    """ continuous integration configuration class """
    DEBUG = True


class TestingConfig(Config):
    """ testing configuration class """
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """ production configuration class """
    DEBUG = True


config_by_name = dict(
    development=DevelopmentConfig,
    ci=ContinuousIntegrationConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
