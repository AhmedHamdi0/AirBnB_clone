#!/usr/bin/python3

"""Defines the State class."""

from models.base_model import BaseModel


class State(BaseModel):
    """A class representing a state."""

    name: str = ""
