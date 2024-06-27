#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv

class Review(BaseModel, Base):
    """Representation of Review """
    product_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
