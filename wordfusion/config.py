# -*- coding: utf-8 -*-

from os import path

from wordfusion import app

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///' + path.join(app.instance_path, 'wordfusion.db')

class Development(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///' + path.join(app.instance_path, 'development.db')

class Testing(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite:///' + path.join(app.instance_path, 'testing.db')
