# -*- coding: utf-8 -*-

from flask import render_template

from wordfusion import app
from wordfusion.database import db_session
from wordfusion.models import Session

@app.route('/sessions')
def show_session_list():
    '''Show the list of sessions.'''
    session_list = db_session.query(Session).all()
    return render_template('list_sessions.html', session_list=session_list)

@app.route('/session/<int:session_id>')
def show_session(session_id):
    '''Show information of the session.'''
    session_object = db_session.query(Session).filter(Session.id == session_id).first()
    return render_template('show_session.html', session_object=session_object)
