#!/usr/bin/python3
""" Define ciy class """

from models.base_model import BaseModel


class City(BaseModel):
    """ City class """
    state_id = ""
    name = ""