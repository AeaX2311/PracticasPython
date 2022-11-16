class BaseConfig:
    USER_DB = 'postgres';
    PASS_DB = 'SA';
    URL_DB = '127.0.0.1';
    NAME_DB = 'clase_login';
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}';
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB;
    SECRET_KEY = 'QWAD23QD35FDSFF4WRFDVRE4T346';
    DEBUG = False;
    BCRYPT_LOG_ROUNDS = 15; # 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False;

