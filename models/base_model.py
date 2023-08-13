#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all other classes with common attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        d_f = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                self.created_at = datetime.strptime(kwargs.get('created_at'), d_f)
                self.updated_at = datetime.strptime(kwargs.get('updated_at'), d_f)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a formatted string indicating the class name, id and dictionary
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Update the 'updated_at'the current datetime.
        This method indicates that the object has been modified.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the object's attributes to a dictionary.
        Return a dictionary containing object attributes for serialization.
        """
        data = self.__dict__.copy()
        data['__class__'] = type(self).__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
