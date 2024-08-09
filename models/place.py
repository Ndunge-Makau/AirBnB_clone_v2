#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
import models
from models.amenity import Amenity


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', cascade='delete', backref='place')


    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            my_list = []
            for review in models.storage.all(Review).values():
                if review.state_id == self.id:
                    my_list += review
            return my_list
        @property
        def amenities(self):
            return self.amenity_ids
        @amenities.setter
        def amenities(self, obj):
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)


    else:
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False, back_populates="place_amenities")

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))