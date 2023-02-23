#!/usr/bin/python3
"""Test Modules"""
import io
import sys
import unittest
import os
import datetime
from models.place import Place
from models import storage


class TestUser(unittest.TestCase):

    def test_attributes(self):
        base1 = Place()
        base2 = Place()
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)

    def test_attribute_type(self):
        base1 = Place()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime.datetime)
        self.assertEqual(type(base1.updated_at), datetime.datetime)

    def test_storage(self):
        base = Place()
        self.assertNotEqual(len(storage.all()), 0)
