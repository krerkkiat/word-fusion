# -*- coding: utf-8 -*-
'''Database module.
It define the db_session for the connection.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from wordfusion import app

engine = create_engine(app.config['DATABASE_URI'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,\
                                         autoflush=False,\
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    '''To populate the databse with tables.'''
    import wordfusion.models
    Base.metadata.create_all(bind=engine)
