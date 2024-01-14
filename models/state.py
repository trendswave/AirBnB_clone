#!/usr/bin/python3

from base_model import BaseModel

class User(BaseModel):
    """Manages the State of the user. It inherits from BaseModel."""
    name: str = ""
