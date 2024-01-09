#!usr/bin/python3
"""Defines a class BaseModel"""
import datetime
import json
import uuid


class BaseModel():

    def __init__(self, ):
        """Initialize a BaseModel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{__class__.__name__} ({self.id}) {self.__dict__}"

    def save(self):
        """update the public instance attribute"""
        pass

    def to_dict(self):
        """returns a dicitionary containing all keys/values of the objece"""
        
        return { 'id' : self.id,
                'class':__class__,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()
            }