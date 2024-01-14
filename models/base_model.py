#!/usr/bin/python3
"""Defines a class BaseModel"""
import models
from datetime import datetime
import uuid


class BaseModel():
    """BaseModel: representation of the project's parent class"""
    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """return the string format of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dicitionary containing all keys/values of the object"""
        target_dict = {k: v for k, v in self.__dict__.items()}
        target_dict['created_at'] = self.created_at.isoformat()
        target_dict['updated_at'] = self.updated_at.isoformat()
        target_dict['__class__'] = self.__class__.__name__
        return target_dict
