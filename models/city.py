#!/usr/bin/python3
"""
City Module

This module defines the City class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class."""
    def __init__(self, *args, **kwargs):
        """Initialization method."""
        super().__init__(*args, **kwargs)
        # Puedes agregar inicializaciones específicas de la clase City aquí

    # Puedes agregar otros métodos y propiedades específicos de la clase City según sea necesario

