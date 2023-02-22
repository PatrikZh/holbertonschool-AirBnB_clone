#!/usr/bin/python3
'''Engine Module'''
import json
import os
from models.base_model import BaseModel

class FileStorage:
    '''Class used to manipulate json obj'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            new_dict = {}
            x = self.all()
            for element in x:
                new_dict[element] = x[element].to_dict()
            f.write(json.dumps(new_dict))

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                content = f.read()
                if len(content) != 0:
                    obj = json.loads(content)
                    for key, value in obj.items():
                        value = eval(value['__class__'])(**value)
                        FileStorage.new(self, value)
