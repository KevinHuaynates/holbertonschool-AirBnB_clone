#!/usr/bin/python3
"""
User Module

This module defines the User class, which inherits from BaseModel.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """User class."""
    def __init__(self, *args, **kwargs):
        """Initialization method."""
        super().__init__(*args, **kwargs)
        # Aquí puedes agregar inicializaciones específicas de la clase User

    # Puedes agregar aquí otros métodos y propiedades específicos de la clase User según sea necesario

