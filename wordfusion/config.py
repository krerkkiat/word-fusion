# -*- coding: utf-8 -*-
'''Configuration module of Word Fusion.'''

from os import path

from wordfusion import app

class Config(object):
    '''A base configuration class.'''
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///' + path.join(app.instance_path, 'wordfusion.db')

class Development(Config):
    '''A set of configuration for development.'''
    DEBUG = True
    DATABASE_URI = 'sqlite:///' + path.join(app.instance_path, 'development.db')

class Testing(Config):
    '''A set of configuration for testing.'''
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite:///' + path.join(app.instance_path, 'testing.db')
