#!/usr/bin/python3

"""Defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """A class representing a city."""

    state_id: str = ""
    name: str = ""
