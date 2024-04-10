import unittest

from models.base_model import BaseModel
"""Defines BaseModel Testing Class."""


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))
