#!/usr/bin/python3

from base_model import BaseModel

class User(BaseModel):
    
    '''This collect the city the user is in'''  
    city: str = ""
    state_id: str = ""