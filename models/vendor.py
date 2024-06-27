#!/usr/bin/env python3
from models.base_model import Basemodel


class Vendor(BaseModel):
    """The vendor class"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """User class initialized """
        super().__init__(*args, **kwargs)
