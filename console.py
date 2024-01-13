#!/usr/bin/python3
#command interpreter in python

import cmd
# print(dir(cmd.Cmd))

'''class for command interpter '''
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models import classes, storage
import re
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models

class Command(cmd.Cmd):
    intro = 'Welcome to the command prompt! Please enter help for a list of commands.'
    prompt = '(hbnb) '
    
    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True
    
    def do_quit(self, line):
        ''' This is to exit the custom CMD'''
        return True
    pass
Command().cmdloop()

def do_create(self, arg):
        'Creates new instance'
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj = classes[args[0]]()
            obj.save()
            print(obj.id)             