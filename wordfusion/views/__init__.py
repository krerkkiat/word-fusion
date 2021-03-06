# -*- coding: utf-8 -*-
'''Views of Word Fusion.'''

from wordfusion import app
from wordfusion.models import CompoundWord
from wordfusion.database import db_session
from wordfusion.views.session import *
from wordfusion.views.wordset import *

@app.route('/')
def index():
    '''Show the index page.'''
    return 'Word Fusion'

@app.route('/search/<word>')
def search(word):
    '''Serve the word information.
    The game page will use this to find other word that is
    not originally in the word set.
    '''
    words = db_session.query(CompoundWord).filter(CompoundWord.combination == word).all()

    res = []
    for word in words:
        obj = {}
        obj['full_word'] = word.combination
        obj['description'] = word.description
        res.append(obj)

    response = make_response(json.dumps(res), 200)
    response.headers['Content-Type'] = 'text/json; charset=utf-8'

    return response
