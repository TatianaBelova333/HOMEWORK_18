# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.
class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 3, 'sort_keys': False}