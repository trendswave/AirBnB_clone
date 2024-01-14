import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
class _FileStorage:

    '''Class for storing and reciving data'''

CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }
__file_path = "file.json" #The json file path
__objects = {} #dictionary to score all object by name.id

def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id"'''
        key = "{}.{}".format (obj.__class_._name_, obj.id)
        self.__objects[key] = obj
        
def all(self):
        '''Retrives all the dictionaries. __object'''
        return self.__objects
        
def save(self):
    ''' Serilize the __object dic. to a json format'''
    serialized_objects = {}
    for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

    with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)    
        
def reload(self):
    '''Deserilize the json file, to a python object'''
    if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                serialized_objects = json.load(file)
                for key, obj_data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create an instance of
                    # the class based on class_name
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**obj_data)
                    # Store the instance in __objects
                    self.__objects[key] = obj_instance    
                        