#!/usr/bin/python3
"""Test Modules"""
import io
import sys
import unittest
import os
import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):

    def test_storage(self):
        obj = FileStorage()
        self.assertEqual(type(obj.all()), dict)

    def test_new(self):
        obj = FileStorage()
        base = BaseModel()
        for value in obj.all().values():
            if base == obj:
                self.assertEqual(base, value)

    def test_filepath(self):
        obj = FileStorage()
        self.assertEqual(obj._FileStorage__file_path, "file.json")
