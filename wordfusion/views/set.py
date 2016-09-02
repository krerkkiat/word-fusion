# -*- coding: utf-8 -*-
import json

from flask import render_template, make_response

from wordfusion import app
from wordfusion.database import db_session
from wordfusion.models import Set

@app.route('/sets')
def show_set_list():
    '''Show the list of sets.'''
    set_list = db_session.query(Set).all()
    return render_template('list_sets.html', set_list=set_list)

@app.route('/set/<int:set_id>')
def show_set(set_id):
    '''Show a set.'''
    set_object = db_session.query(Set).filter(Set.id == set_id).first()
    return render_template('show_set.html', set_object=set_object)

@app.route('/set/<int:set_id>/words')
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

@app.route('/set/<int:set_id>/play', methods=['GET'])
def play_set(set_id):
    '''Serve the html for the wordfusion page.'''
    return render_template('word_fusion.html', set_id=set_id)
