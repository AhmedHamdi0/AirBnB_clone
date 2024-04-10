#!/usr/bin/python3

"""Defines the Place class."""

from models.base_model import BaseModel

class Place(BaseModel):
    """A class representing a place."""

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list[str] = []

    def __init__(self, *args, **kwargs):
        """Initialize a new Place object."""
        super().__init__(*args, **kwargs)
