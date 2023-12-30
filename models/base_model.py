#!/usr/bin/python3
"""
Base Model Module

This module defines the BaseModel class.
"""

import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class."""
    def __init__(self, *args, **kwargs):
        """Initialization method."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # Agrega aquí otros métodos y propiedades de la clase BaseModel según sea necesario

