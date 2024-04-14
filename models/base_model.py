#!/usr/bin/python3

"""Define Base Model Class."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for models with unique IDs and timestamps."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' timestamp to the current time."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """returns a dictionary containing all keys/values of __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
