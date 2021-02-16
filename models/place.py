#!/usr/bin/python3
""" Module for class Place that
inherits from BaseModel """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class Place that inherits from BaseModel """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
