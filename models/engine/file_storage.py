#!/usr/bin/python3

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
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to JSON file (__file_path)."""
        with open(self.__file_path, 'w') as file:
            serialized_objects = {key: obj.to_dict()
                                  for key, obj in self.__objects.items()}
            json.dump(serialized_objects, file, indent=4)

    def reload(self):
        """Deserialize JSON file to __objects (if file exists)."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**obj_dict)
        except FileNotFoundError:
            pass
