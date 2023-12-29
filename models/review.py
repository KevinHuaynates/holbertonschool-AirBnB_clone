#!/usr/bin/python3
"""
Module para Review class.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Class Review que hereda BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

