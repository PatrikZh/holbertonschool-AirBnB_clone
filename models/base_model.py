#!/usr/bin/python3
''' Module of base class'''
import uuid
from datetime import datetime


class BaseModel:
    '''Base model class'''
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        ''' Printing string repr of instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' update time'''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' dict repr of instance'''
        new_d = {}
        new_d = self.__dict__.copy()
        new_d["__class__"] = str(self.__class__.__name__)
        new_d['created_at'] = self.created_at.isoformat()
        new_d['updated_at'] = self.updated_at.isoformat()
        return new_d
