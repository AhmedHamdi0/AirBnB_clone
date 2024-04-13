#!/usr/bin/python3

"""Define Base Model Class."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for models with unique IDs and timestamps."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.__dict__.update({'created_at': datetime.fromisoformat(value)})
                elif key == 'updated_at':
                    self.__dict__.update({'updated_at': datetime.fromisoformat(value)})
                else:
                    self.__dict__.update({key: value})
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """Return a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the 'updated_at' timestamp to the current time."""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the BaseModel instance
        with class name and timestamps.
        """
        obj_dict = {}
        obj_dict.update({'__class__': self.__class__.__name__})
        obj_dict.update(self.__dict__)
        obj_dict.update({'created_at': self.created_at.isoformat(),
                         'updated_at': self.updated_at.isoformat()})
        return obj_dict
