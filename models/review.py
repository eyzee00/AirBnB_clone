#!/usr/bin/python3
"""Module: defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review: defines a Review object"""
    place_id = ""
    user_id = ""
    text = ""
