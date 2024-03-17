#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel, Base):
    """ class amenity """
    __tablename__ = "amenities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
