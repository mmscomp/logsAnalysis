import sys, psycopg2

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import ceclarative_base
from sqlalchemy,orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

Class Articles(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    author = Column(String(300), nullable=False)
    title = Column(String(300), nullable=False)
    slug = Column(String(300), nullable=False)
