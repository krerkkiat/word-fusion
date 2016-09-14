# -*- coding: utf-8 -*-

import json

from wordfusion.database import db_session
from wordfusion.models import *

def seed_db():
    from wordfusion.models import User, WordSet, CompoundWord
    from wordfusion.database import db_session

    user = User(username='foobar', first_name='Foo', last_name='bar')
    db_session.add(user)
    db_session.commit()

    with open('seeding/seed_data.json') as f:
        data = json.load(f)

        if 'sets' in data.keys():
            for s in data['sets']:
                word_set = WordSet(name=s['name'], description=s['description'])
                for cw in s['compound_words']:
                    compound_word = CompoundWord(text_th=cw['text_th'],\
                                                 text_eng=cw['text_eng'],\
                                                 description=cw['description'],\
                                                 part_of_speech=cw['part_of_speech'],\
                                                 combination=cw['combination'])

                    word_set.compound_words.append(compound_word)

                db_session.add(word_set)

            db_session.commit()
        if 'sessions' in data.keys():
            for s in data['sessions']:
                session_object = Session(name=s['name'],\
                                         description=s['description'],\
                                         condition='test condition',\
                                         active=s['active'])
                #
                db_session.add(session_object)
            db_session.commit()

if __name__ == '__main__':
    from wordfusion.database import init_db

    init_db()
    seed_db()
