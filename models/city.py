#!/usr/bin/python3
"""Handles the City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    The City Class
    ========================
    Inherits from BaseModel.
    ========================

    Public Class Attributes:
        name: string - empty string
        state_id: string - empty string: it will be the State.id
    """
    name = ""
    state_id = ""
