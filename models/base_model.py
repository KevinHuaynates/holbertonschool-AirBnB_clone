#!/usr/bin/python3
"""BaseModel module"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for AirBnB objects."""
    def __init__(self, *args, **kwargs):
        """Initialization method."""
        pass

    def save(self):
        """Save the current instance to a JSON file."""
        pass

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        pass
