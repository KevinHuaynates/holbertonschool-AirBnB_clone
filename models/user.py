#!/usr/bin/python3
"""Module para User class."""
from models.base_model import BaseModel

class User(BaseModel):
    """User class que hereda BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

