#!/usr/bin/python3

"""Defines test cases for the User class."""

import os
import unittest
from datetime import datetime

from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Test cases for instantiating the User class."""

    def setUp(self):
        """Set up test environment before each test method."""
        self.obj = User()

    def test_instance_type(self):
        """Test if the object is an instance of the User class."""
        self.assertEqual(type(self.obj), User)

    def test_insatance_attributes_exits(self):
        """Test if instance attributes exist."""
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))
        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'password'))

    def test_instance_attributes_types(self):
        """Test if instance attributes have the correct data types."""
        self.assertEqual(type(self.obj.created_at), datetime)
        self.assertEqual(type(self.obj.updated_at), datetime)
        self.assertEqual(type(self.obj.id), str)
        self.assertEqual(type(self.obj.first_name), str)
        self.assertEqual(type(self.obj.last_name), str)
        self.assertEqual(type(self.obj.email), str)
        self.assertEqual(type(self.obj.password), str)

    def test_two_instances_has_unique_ids(self):
        """Test if two instances have unique IDs."""
        obj1 = User()
        obj2 = User()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_assign_id_attr(self):
        """Test assigning a value to the 'id' attribute."""
        obj = User()
        obj.id = 10
        self.assertEqual(obj.id, 10)

    def test_assign_created_at_attr(self):
        """Test assigning a value to the 'created_at' attribute."""
        obj = User()
        date_time = datetime(2001, 10, 18, 8, 30, 30, 50)
        obj.created_at = date_time
        self.assertEqual(obj.created_at, date_time)

    def test_assign_update_at_attr(self):
        """Test assigning a value to the 'updated_at' attribute."""
        obj = User()
        date_time = datetime(2001, 10, 18, 8, 30, 30, 50)
        obj.updated_at = date_time
        self.assertEqual(obj.updated_at, date_time)

    def test_assign_review_instance_attrs(self):
        """Test assigning a value to the 'review' attribute."""
        obj = User()
        obj.first_name = 'First'
        obj.last_name = 'Last'
        obj.email = 'mail@example.com'
        obj.password = 'root'
        self.assertEqual(obj.first_name, 'First')
        self.assertEqual(obj.last_name, 'Last')
        self.assertEqual(obj.email, 'mail@example.com')
        self.assertEqual(obj.password, 'root')

    def test_created_at_and_updated_at_are_at_creation(self):
        """Test if 'created_at' and 'updated_at' are equal at creation."""
        self.assertEqual(self.obj.created_at, self.obj.updated_at)

    def test_str_representation(self):
        """Test the string representation of the object."""
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        obj = User()
        obj.id = "123456"
        obj.created_at = obj.updated_at = date_time
        obj_repr = obj.__str__()
        self.assertIn("[User] (123456)", obj_repr)
        self.assertIn("'id': '123456'", obj_repr)
        self.assertIn("'created_at': " + date_time_repr, obj_repr)
        self.assertIn("'updated_at': " + date_time_repr, obj_repr)

    def test_obj_args_unused(self):
        """Test object instantiation with unused arguments."""
        obj = User(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test object instantiation with keyword arguments."""
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        obj = User(id="345", created_at=date_time_iso,
                   updated_at=date_time_iso)
        self.assertEqual(obj.id, "345")
        self.assertEqual(obj.created_at, date_time)
        self.assertEqual(obj.updated_at, date_time)

    def test_instantiation_with_None_kwargs(self):
        """Test object instantiation with None keyword arguments."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        """Test obj instantiation with positional and keyword arguments."""
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        obj = User("22", id="345", created_at=date_time_iso,
                   updated_at=date_time_iso)
        self.assertEqual(obj.id, "345")
        self.assertEqual(obj.created_at, date_time)
        self.assertEqual(obj.updated_at, date_time)


class TestUserSave(unittest.TestCase):
    """Test cases for saving User instances."""

    def setUp(self):
        """Set up test environment before each test method."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Clean up test environment after each test method."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_id(self):
        """Test saving an object with an existing ID."""
        obj = User()
        old_id = obj.id
        obj.save()
        self.assertEqual(obj.id, old_id)

    def test_save_with_created_at(self):
        """Test saving an object without updating 'created_at'."""
        obj = User()
        old_created_at = obj.created_at
        obj.save()
        self.assertEqual(obj.created_at, old_created_at)

    def test_save_with_updated_at(self):
        """Test saving an object with updated 'updated_at'."""
        obj = User()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_save_with_arg(self):
        """Test saving an object with an argument."""
        obj = User()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        """Test if saving updates the file."""
        obj = User()
        obj.save()
        obj_id = "User." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())


class TestUserToDict(unittest.TestCase):
    """Test cases for converting User instances to dictionaries."""

    def setUp(self):
        """Set up test environment before each test method."""
        self.obj = User()

    def test_to_dict_type(self):
        """Test the type of the converted dictionary."""
        self.assertTrue(dict, type(self.obj.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the converted dictionary contains the correct keys."""
        self.assertIn("id", self.obj.to_dict())
        self.assertIn("created_at", self.obj.to_dict())
        self.assertIn("updated_at", self.obj.to_dict())
        self.assertIn("__class__", self.obj.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the converted dictionary contains added attributes."""
        self.obj.name = "Hellp"
        self.obj.age = 22
        self.assertIn("name", self.obj.to_dict())
        self.assertIn("age", self.obj.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes in the dictionary are strings."""
        obj_dict = self.obj.to_dict()
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of the to_dict method."""
        date_time = datetime.today()
        obj = User()
        obj.id = "123456"
        obj.created_at = obj.updated_at = date_time
        obj_dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }
        self.assertDictEqual(obj.to_dict(), obj_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test the difference between to_dict and __dict__."""
        self.assertNotEqual(self.obj.to_dict(), self.obj.__dict__)

    def test_to_dict_with_arg(self):
        """Test to_dict method with an argument."""
        self.obj = User()
        with self.assertRaises(TypeError):
            self.obj.to_dict(None)


if __name__ == "__main__":
    unittest.main()
