#!/usr/bin/python3

"""Defines the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class representing an amenity."""

    name: str = ""

    def __init__(self, *args, **kwargs):
        """create new Amenity"""
        super().__init__(self, *args, **kwargs)
