#!/usr/bin/python3
""" User Class """

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''subclass of BaseModel class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
