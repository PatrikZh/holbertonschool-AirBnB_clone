#!/usr/bin/python3
"""Module of Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    ''' city_id will be the same as City.id'''
    city_id = ''
    ''' user_id will be the same as User.id'''
    user_id = ''
    text = ''
