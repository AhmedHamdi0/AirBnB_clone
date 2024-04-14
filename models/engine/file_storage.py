#!/usr/bin/python3

"""Defines the FileStorage class."""

import json
import os

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Serialize instances to a JSON file and
    deserialize JSON file to instances.
    """

    __file_path: str = 'file.json'
    __objects: dict = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """Return the dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file (__file_path)."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            data = {key: value.to_dict()
                    for key, value in FileStorage.__objects.items()}
            json.dump(data, file, indent=4)

    def reload(self):
        """Deserialize JSON file to __objects (if file exists)."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {key: FileStorage.classes[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict
