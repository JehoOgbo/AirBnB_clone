#!/usr/bin/python3
'''Child to BaseModel class'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''Inherits from basemodel and has a public attribute'''
    place_id = ""
    user_id = ""
    text = ""
