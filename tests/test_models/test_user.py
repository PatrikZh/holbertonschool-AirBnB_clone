#!/usr/bin/python3
"""Test Modules"""
import io
import sys
import unittest
import os
import datetime
from models.user import User
from models import storage


class TestUser(unittest.TestCase):

    def test_attributes(self):
        base1 = User()
        base2 = User()
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)

    def test_attribute_type(self):
        base1 = User()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime.datetime)
        self.assertEqual(type(base1.updated_at), datetime.datetime)

    def test_email(self):
        base = User()
        email = "someone@email.com"
        base.email = email
        self.assertEqual(base.email, email)

    def test_password(self):
        base = User()
        self.assertEqual(base.password, '')

    def test_user_first_name_last_name(self):
        base = User()
        first_name = "Fabio"
        last_name = "Njishi"
        base.first_name = first_name
        base.last_name = last_name
        self.assertEqual(base.first_name, first_name)
        self.assertEqual(base.last_name, last_name)
