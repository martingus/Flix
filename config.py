import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-my-secret-key'
    FLIX_USER = os.environ.get('FLIX_USER')
    FLIX_PWD = os.environ.get('FLIX_PWD')