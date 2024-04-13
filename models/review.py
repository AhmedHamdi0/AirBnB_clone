#!/usr/bin/python3

"""Defines the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class representing a review."""

    place_id: str = ""
    user_id: str = ""
    text: str = ""

    def __init__(self, *args, **kwargs):
        """create new Review"""
        super().__init__(self, *args, **kwargs)
