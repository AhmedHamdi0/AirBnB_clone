#!/usr/bin/python3

"""Defines the FileStorage class."""

import json
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

    def all(self):
        """Return the dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to JSON file (__file_path)."""
        objs_dict = FileStorage.__objects
        serialized_objects = {obj: objs_dict[obj].to_dict() for obj in objs_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserialize JSON file to __objects (if file exists)."""
        try:
            with open(FileStorage.__file_path) as f:
                objs_dict = json.load(f)
                for obj in objs_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
