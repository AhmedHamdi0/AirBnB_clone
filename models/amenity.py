#!/usr/bin/python3

"""Defines the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class representing an amenity."""

    name: str = ""
