# -*- coding: utf-8 -*-
'''Word Fusion.'''

from flask import Flask

app = Flask(__name__)
app.config.from_object('wordfusion.config.Development')

import wordfusion.views
from wordfusion.database import db_session
from wordfusion.blueprints.matchinggame import matchinggame

app.register_blueprint(matchinggame, url_prefix='/<type>/<int:word_set_id>')

@app.teardown_appcontext
def shutdown_database_session(exception=None):
    db_session.remove()
