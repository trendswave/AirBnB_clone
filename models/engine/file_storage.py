import json
import os
from models.base_module import BaseModel

class FileStorage:
    '''Class for storing and reciving data'''
    __file_path = "file.json" 
    __objects = {}

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id"'''
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format (obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj
        
    def all(self):
        '''Retrives all the dictionaries. __object'''
        return FileStorage.__objects
        
    def save(self):
        ''' Serilize the __object dic. to a json format'''
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()
            
        with open (FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)
    def reload(self):
        '''Deserilize the json file, to a python object'''
        if os.path.isfile(FileStorage.__file.path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        cls_name, obj_id = key.split(".")
                        cls = eval(cls_name)
                        
                        instance = cls(**value)
                        
                        FileStorage.__objects[key] = instance
                        
                except Exception:
                    pass
                        