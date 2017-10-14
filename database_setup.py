import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Erretem(Base):
	__tablename__ = 'erretem'
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False )

class MenuItem(Base):
	__tablename__ = 'menuItem'
	id = Column(Integer, primary_key = True)
	name = Column(Integer, nullable = False)
	description = Column(String(250))
	price = Column(String(8))
	course = Column(String(250))
	erretem_id = Column(Integer, ForeignKey(Erretem.id))
	erretem = relationship(Erretem)

engine = create_engine('sqlite:///erretemMenu.db')
Base.metadata.create_all(engine)
	
