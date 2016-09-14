# -*- coding: utf-8 -*-
'''Word Set related views.'''
import json

from flask import render_template, make_response, request

from wordfusion import app
from wordfusion.database import db_session
from wordfusion.models import WordSet

@app.route('/word_sets')
def show_word_set_list():
    '''Show the list of word sets.'''
    word_sets = db_session.query(WordSet).all()
    return render_template('list_word_sets.html', word_sets=word_sets)

@app.route('/word_set/<int:word_set_id>', methods=['GET', 'POST'])
def show_word_set(word_set_id):
    '''Show a set of words.'''

    if request.method == 'GET':
        word_set = db_session.query(WordSet).filter(WordSet.id == word_set_id).first()
        return render_template('show_word_set.html', word_set=word_set)
    elif request.method == 'POST':
        pass
