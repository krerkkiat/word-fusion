# -*- coding: utf-8 -*-
'''Blueprint for Matching Game.
A Word Set and Session should have play,
and list_words.
'''

import json

from flask import Blueprint, render_template, make_response

from wordfusion.database import db_session
from wordfusion.models import WordSet

matchinggame = Blueprint('matchinggame', __name__, template_folder='templates')

@matchinggame.route('/play')
def play(type, word_set_id):
    '''Serve the html for the wordfusion page.'''
    return render_template('matchinggame/game.html', word_set_id=word_set_id)

@matchinggame.route('/words')
def list_words(type, word_set_id):
    '''List all words in the word set.'''
    set_object = db_session.query(WordSet).filter(WordSet.id == word_set_id).first()

    words_list = []
    for word in set_object.compound_words:
        word_obj = {}
        word_obj['full_word'] = word.combination
        word_obj['description'] = word.description
        words_list.append(word_obj)

    response = make_response(json.dumps(words_list), 200)
    response.headers['Content-Type'] = 'text/json; charset=utf-8'

    return response
