import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    # id = Column(Integer, primary_key=True)
    # name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    # id = Column(Integer, primary_key=True)
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    latitude = Column(Integer)
    longitude = Column(Integer)
    climate = Column(String(250))
    galaxy = Column(String(250))
    inhabited = Column(Boolean)


class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    home_planet = Column(String(250), ForeignKey('planets.id'))
    species = Column(String(250))
    faction = Column(String(250))


class Favorites(Base):
    __tablename__= 'favorites'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    fav_planets = Column(String(250), ForeignKey('planets.name'))
    fav_characters = Column(String(250), ForeignKey('characters.name'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
