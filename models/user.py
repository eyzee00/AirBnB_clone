#!/usr/bin/python3
"""Module: Defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User: defines a User object"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
