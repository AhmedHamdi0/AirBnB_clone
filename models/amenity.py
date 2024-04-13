#!/usr/bin/python3

"""Defines the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class representing an amenity."""

    name: str = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity object."""
        super().__init__(*args, **kwargs)
