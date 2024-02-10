#!/usr/bin/python3
'''Child to BaseModel class'''

from models.base_model import BaseModel


class City(BaseModel):
    '''Inherits from basemodel and has a public attribute'''
    state_id = ""
    name = ""
