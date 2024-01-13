#!/usr/bin/python3
"""Module: defines the Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place: defines a Place object"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    altitude = 0.0
    amenity_ids = []
