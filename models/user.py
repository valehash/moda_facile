#!/usr/bin/python3
"""The user class"""
from models.base_model import BaseModel

class User(BaseModel):
    """The user class"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """User class initialized """
        super().__init__(*args, **kwargs)
