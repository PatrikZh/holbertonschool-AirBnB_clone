#!/usr/bin/python3
''' Module of base class'''
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.id = str(uuid.uuid4())
            self.created_at = (datetime.strptime(
                datetime.now().isoformat(), '%Y-%m-%dT%H:%M:%S.%f'))
            self.updated_at = (datetime.strptime(
                datetime.now().isoformat(), '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = str(datetime.now().isoformat())

    def to_dict(self):
        new_d = {}
        new_d = self.__dict__.copy()
        new_d["__class__"] = self.__class__.__name__
        return new_d
