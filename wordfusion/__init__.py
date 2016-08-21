# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
app.config.from_object('wordfusion.config.Development')

import wordfusion.views
from wordfusion.database import db_session

@app.teardown_appcontext
def shutdown_database_session(exception=None):
    db_session.remove()
