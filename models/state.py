#!/usr/bin/python3
"""
State Module

This module defines the State class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class."""
    def __init__(self, *args, **kwargs):
        """Initialization method."""
        super().__init__(*args, **kwargs)
        # Puedes agregar inicializaciones específicas de la clase State aquí

    # Puedes agregar otros métodos y propiedades específicos de la clase State según sea necesario

