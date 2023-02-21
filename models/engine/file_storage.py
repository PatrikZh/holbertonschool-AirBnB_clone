#!/usr/bin/python3
'''Engine Module'''
import json

class FileStorage:
    '''Class used to manipulate json obj'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if type(obj) is dict:
            key = f"BaseModel.{obj['id']}"
            FileStorage.__objects[key] = obj
        else:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            # for key, value in FileStorage.__objects.items():
            #     print(value)
            #     FileStorage.__objects[key] = value
            f.write(json.dumps(self.all()))

    def reload(self):
        if FileStorage.__file_path:
            with open(FileStorage.__file_path, 'r') as f:
                content = f.read()
                if len(content) != 0:
                    obj = json.loads(content)
                    print(obj)
                    for key, value in obj.items():
                        FileStorage.new(self, value)
