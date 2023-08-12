#!/usr/bin/python3
"""Handles the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review Class
    ========================
    Inherits from BaseModel.
    ========================

    Public Class Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string

    """
    place_id = ""
    user_id = ""
    text = ""

    def to_dict(self):
        """Convert the object's attributes to a dictionary."""
        data = super().to_dict()
        data['place_id'] = self.place_id
        data['user_id'] = self.user_id
        data['text'] = self.text
        return data
