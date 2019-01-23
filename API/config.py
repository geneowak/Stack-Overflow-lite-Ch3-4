import os


class DefaultConfig(object):
    """ Default configurations """
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    # Put any configurations here that are common across all environments


class TestingConfig(DefaultConfig):
    """ Configurations for Testing, with a separate test database."""
    TESTING = True


class DevelopmentConfig(DefaultConfig):
    """ Development configurations """
    DEBUG = True


class ProductionConfig(DefaultConfig):
    """ Production configurations """
    DEBUG = False


app_config = {
    'default': DefaultConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
