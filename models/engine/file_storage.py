import json
import models
from models.base_model import BaseModel


class FileStorage:
    """Handles a=how classes are loaded into the objects and unloaded"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """function to display all the objects in the dictionary"""
        return self.__objects
    
    def new(self, obj):
        """adds a new object to the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """save function to the dictionary to a json"""
        new_dict = {}
        for objects, val in self.__objects.items():
            new_dict[objects] = val.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """converts the file json to objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obs = json.load(f)
                for key, value in obs.items():
                    vals = eval(f"{value['__class__']}(**value)")
                    self.__objects[key] = vals
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

