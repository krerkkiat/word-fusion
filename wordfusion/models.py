# -*- coding: utf-8 -*-
'''Models of the Word Fusion.'''

import enum

from sqlalchemy import Column, String, Integer, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship, backref

from wordfusion.database import Base

class PartOfSpeech(enum.Enum):
    '''Define the part of speech of word.'''
    noun = 'noun'
    verb = 'verb'
    adjective = 'adjective'
    adverb = 'adverb'

class User(Base):
    '''A mapper for User.'''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    word_sets = relationship('WordSet', back_populates='user')
    sessions = relationship('Session', back_populates='user')

    def __repr__(self):
        return '<User: %r>' % (self.username)

class WordSet(Base):
    '''A mapper for Word Set.'''
    __tablename__ = 'word_sets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='word_sets')

    compound_words = relationship('CompoundWord', back_populates='word_set')

class Word(Base):
    '''A mapper for Word.'''
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    text_th = Column(String)
    text_eng = Column(String)
    description = Column(String)
    part_of_speech = Column(Enum(PartOfSpeech))

class CompoundWord(Base):
    '''A mapper for Compound Word.'''
    __tablename__ = 'compound_words'
    id = Column(Integer, primary_key=True)
    text_th = Column(String)
    text_eng = Column(String)
    description = Column(String)
    part_of_speech = Column(Enum(PartOfSpeech))
    combination = Column(String)

    word_set_id = Column(Integer, ForeignKey('word_sets.id'))
    word_set = relationship('WordSet', back_populates='compound_words')

class Session(Base):
    '''A mapper for Session.'''
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    condition = Column(String)
    active = Column(Boolean)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='sessions')
