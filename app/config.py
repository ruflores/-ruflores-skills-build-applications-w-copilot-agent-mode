class DevelopmentConfig:
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig:
    DEBUG = False
    DATABASE_URI = 'mysql://user:password@localhost/prod'

class TestingConfig:
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite:///test.db'