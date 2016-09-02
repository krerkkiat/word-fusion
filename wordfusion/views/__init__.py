# -*- coding: utf-8 -*-

from wordfusion import app
from wordfusion.models import Set
from wordfusion.database import db_session
from wordfusion.views.session import *
from wordfusion.views.set import *

@app.route('/')
def index():
    '''Show the index page.'''
    return 'Word Fusion'
