#!/usr/bin/python3
#command interpreter in python

import cmd
# print(dir(cmd.Cmd))

'''class for command interpter '''
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