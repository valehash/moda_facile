#!/usr/bin/python3

from datetime import datetime
import uuid
import models
import sqlalchemy
from sqlalchemy import Column, String, Datetime
from sqlalchemy.ext.declarative import declarative_base



class BaseModel:
  """The base model class"""

  def __init__ (self, **kwargs):

    fmt_str = "%Y-%m-%dT%H:%M:%S.%f"
    if (kwargs):
      for key, value in kwargs.items():
        if key != '__class__':
          if key in ["created_at", "updated_at"]:
            value = datetime.strptime(value, fmt_str)
          setattr(self, key, value)
    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


  def save(self):
    self.updated_at =  datetime.now()
    models.storage.new(self)

  def to_dict(self):
    objects_dict =  self.__dict__.copy()
    objects_dict['__class__'] =  self.__class__.__name__
    objects_dict['created_at'] =  objects_dict['created_at'].isoformat()
    objects_dict['updated_at'] =  objects_dict['updated_at'].isoformat()
    return objects_dict

  def __str__(self):
    """String representation of the BaseModel class"""
    return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

  def save(self):
    """updates the attribute 'updated_at' with the current datetime"""
    self.updated_at = datetime.utcnow()
    models.storage.new(self)
    models.storage.save()

  """def to_dict(self, save_fs=None):
    #returns a dictionary containing all keys/values of the instance
    new_dict = self.__dict__.copy()
    if "created_at" in new_dict:
      new_dict["created_at"] = new_dict["created_at"].strftime(time)
    if "updated_at" in new_dict:
      new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
      new_dict["__class__"] = self.__class__.__name__
    if "_sa_instance_state" in new_dict:
      del new_dict["_sa_instance_state"]
      if save_fs is None:
        if "password" in new_dict:
          del new_dict["password"]
        return new_dict
      """
  def delete(self):
      """delete the current instance from the storage"""
      models.storage.delete(self)
