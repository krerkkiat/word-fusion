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
