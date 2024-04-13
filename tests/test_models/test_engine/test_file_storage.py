#!/usr/bin/python3

"""Defines unittests for FileStorage."""

import os
import unittest

import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def setUp(self):
        self.base_model = BaseModel()
        self.user = User()
        self.state = State()
        self.place = Place()
        self.city = City()
        self.amenity = Amenity()
        self.review = Review()
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_instance_private_attributes_types(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        self.assertIn("BaseModel." + self.base_model.id,
                      models.storage.all().keys())
        self.assertIn(self.base_model, models.storage.all().values())
        self.assertIn("User." + self.user.id, models.storage.all().keys())
        self.assertIn(self.user, models.storage.all().values())
        self.assertIn("State." + self.state.id, models.storage.all().keys())
        self.assertIn(self.state, models.storage.all().values())
        self.assertIn("Place." + self.place.id, models.storage.all().keys())
        self.assertIn(self.place, models.storage.all().values())
        self.assertIn("City." + self.city.id, models.storage.all().keys())
        self.assertIn(self.city, models.storage.all().values())
        self.assertIn("Amenity." + self.amenity.id,
                      models.storage.all().keys())
        self.assertIn(self.amenity, models.storage.all().values())
        self.assertIn("Review." + self.review.id, models.storage.all().keys())
        self.assertIn(self.review, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        models.storage.new(self.base_model)
        models.storage.new(self.user)
        models.storage.new(self.state)
        models.storage.new(self.place)
        models.storage.new(self.city)
        models.storage.new(self.amenity)
        models.storage.new(self.review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + self.base_model.id, save_text)
            self.assertIn("User." + self.user.id, save_text)
            self.assertIn("State." + self.state.id, save_text)
            self.assertIn("Place." + self.place.id, save_text)
            self.assertIn("City." + self.city.id, save_text)
            self.assertIn("Amenity." + self.amenity.id, save_text)
            self.assertIn("Review." + self.review.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        models.storage.new(self.base_model)
        models.storage.new(self.user)
        models.storage.new(self.state)
        models.storage.new(self.place)
        models.storage.new(self.city)
        models.storage.new(self.amenity)
        models.storage.new(self.review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + self.base_model.id, objs)
        self.assertIn("User." + self.user.id, objs)
        self.assertIn("State." + self.state.id, objs)
        self.assertIn("Place." + self.place.id, objs)
        self.assertIn("City." + self.city.id, objs)
        self.assertIn("Amenity." + self.amenity.id, objs)
        self.assertIn("Review." + self.review.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
