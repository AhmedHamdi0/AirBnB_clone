#!/usr/bin/python3

"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """A class representing a user."""

    first_name: str = ""
    last_name: str = ""
    email: str = ""
    password: str = ""
