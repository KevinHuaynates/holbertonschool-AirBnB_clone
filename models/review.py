#!/usr/bin/python3
"""
Review Module

This module defines the Review class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class."""
    def __init__(self, *args, **kwargs):
        """Initialization method."""
        super().__init__(*args, **kwargs)
        # Puedes agregar inicializaciones específicas de la clase Review aquí

    # Puedes agregar otros métodos y propiedades específicos de la clase Review según sea necesario

