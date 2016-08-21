# -*- coding: utf-8 -*-

from flask import Flask

from wordfusion.database import db_session

app = Flask(__name__)

import wordfusion.views

@app.teardown_appcontext
def shutdown_database_session(exception=None):
    db_session.remove()
