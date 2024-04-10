#!/usr/bin/python3

import uuid
from datetime import datetime

import models


class BaseModel:
    """Base class for models with unique IDs and timestamps."""

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize a BaseModel instance with a unique
        identifier and timestamps.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            return

        self.__create_instance_from_dict(*args, **kwargs)

    def __str__(self) -> str:
        """Return a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the 'updated_at' timestamp to the current time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the BaseModel instance
        with class name and timestamps.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __create_instance_from_dict(self, *args, **kwargs) -> None:
        """
        Create an instance of the class using a dictionary
        of key-value pairs.
        """
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            if key in ['created_at', 'updated_at']:
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            setattr(self, key, value)
