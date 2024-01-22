#!usr/bin/python3

# from base_model import BaseModel
from base_model import BaseModel
class User(BaseModel):
    '''class to manage user object or create user profile'''
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    password: str = ""
    
            