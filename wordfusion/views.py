# -*- coding: utf-8 -*-

from wordfusion import app

@app.route('/')
def index():
    return 'Word Fusion'
