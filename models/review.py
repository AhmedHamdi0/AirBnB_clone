#!/usr/bin/python3

"""Defines the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class representing a review."""

    place_id: str = ""
    user_id: str = ""
    text: str = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Review object."""
        super().__init__(*args, **kwargs)
