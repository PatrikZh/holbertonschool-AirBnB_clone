#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' city_id will be the same as City.id'''
    city_id = ''
    ''' user_id will be the same as User.id'''
    user_id = ''
    text = ''
