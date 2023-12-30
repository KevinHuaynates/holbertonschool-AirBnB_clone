#!/usr/bin/python3
"""
Amenity Module

This module defines the Amenity class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class."""
    def __init__(self, *args, **kwargs):
        """Initialization method."""
        super().__init__(*args, **kwargs)
        # Puedes agregar inicializaciones específicas de la clase Amenity aquí

    # Puedes agregar otros métodos y propiedades específicos de la clase Amenity según sea necesario

