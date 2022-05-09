import logging

class Config(object):
    """ Global configuration """
    PORT = "5000"
    DEBUG = False
    TESTING = False
    HOST = "127.0.0.1"


class ProductionConfig(Config):
    """ Additional configuration for production system """
    def __init__(self) -> None:
        logging.info('Production configuration')
    pass


class DevelopmentConfig(Config):
    """ Additional configuration for development system """
    def __init__(self) -> None:
        logging.info('Development configuration')
    PORT = "8080"
    DEBUG = True
    HOST = "0.0.0.0"


class TestingConfig(Config):
    """ Additional configuration for test system """
    def __init__(self) -> None:
        logging.info('Test configuration')
    TESTING = True