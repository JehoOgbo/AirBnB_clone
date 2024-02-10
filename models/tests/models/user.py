#!/usr/bin/python3
"""Define the class User"""

from models.base_model import BaseModel


class User(BaseModel):
    '''Defines a user of the basemodel'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
