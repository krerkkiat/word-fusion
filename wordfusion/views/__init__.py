# -*- coding: utf-8 -*-
import json

from flask import render_template, make_response

from wordfusion import app
from wordfusion.models import Set
from wordfusion.database import db_session
from wordfusion.views.session import *

@app.route('/')
def index():
    '''Show the index page.'''
    return 'Word Fusion'

@app.route('/words/<int:set_id>')
def get_words_in_set(set_id):
    '''Show all words in a set in json format.'''
    set_object = db_session.query(Set).filter(Set.id == set_id).first()

    words_list = []
    for word in set_object.compound_words:
        word_obj = {}
        word_obj['full_word'] = word.combination
        word_obj['description'] = word.description
        words_list.append(word_obj)

    response = make_response(json.dumps(words_list), 200)
    response.headers['Content-Type'] = 'text/json; charset=utf-8'

    return response

@app.route('/wordfusion', methods=['GET'])
def wordfusion():
    '''Serve the html for the wordfusion page.'''
    return render_template('word_fusion.html')
