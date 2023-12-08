#!/usr/bin/python3

"""
Module for the class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """The User class

    Args:
        email: the user email
        password: the user password
        first_nmae: the user first_name
        last_name: the user last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialized all superclass args"""
        super().__init__(*args, **kwargs)
