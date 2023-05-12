#!/usr/bin/python3
"""Tnis contains the Place model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Implements the Place model

    Args:
        city_id (str): takes the City id.
        user_id (str): takes the User id.
        name (str): takes the name of the place.
        description (str): takes the description of the place.
        number_rooms (int): takes the number of rooms of the place.
        number_bathrooms (int): takes the number of bathrooms of the place.
        max_guest (int): takes the maximum number of guests of the place.
        price_by_night (int): takes the price by night of the place.
        latitude (float): shows the latitude of the place.
        longitude (float): shows the longitude of the place.
        amenity_ids (list): provides a list of Amenity ids.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
