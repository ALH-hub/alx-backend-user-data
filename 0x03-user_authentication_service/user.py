#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    """ Defines the data model for the table `user`. """
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(520), nullable=True)
