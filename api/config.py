import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_settings(env):
    return eval(env)


class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'APi-Users-123456'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
