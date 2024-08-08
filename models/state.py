#!/usr/bin/python3

""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='delete', backref='state')

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            my_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    my_cities += city
            return my_cities
