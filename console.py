#!/usr/bin/python
'''
    class for command interpter 
'''
import cmd

class HBNBCommand(cmd.Cmd):
    
    '''class for command interpter '''
    prompt = "(hbnb)"
    
    
    def do_EOF(self, line):
        
        """ Handles End Of File character. """
        print()
        return True
    
    def do_quit(self, line):
        
        ''' Quit command to exit the program '''
        return True
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()









# def default(self, arg):
#         """ Deals with <class name>.<command>() """
#         methods = {'all()': "do_all",
#                    'count()': "count",
#                    'create()': "do_create"}
#         tokens = arg.split('.', 1)
#         if tokens[0] not in classes:
#             print("** class doesn't exist **")
#         elif tokens[1] not in methods:
#             print("** command doesn't exist **")
#         else:
#             eval('self.{}("{}")'.format(methods[tokens[1]], tokens[0]))

        
# def parse(arg):
#     return arg.split()

# if __name__ == "__main__":
#     HBNBCommand().cmdloop()def parse(arg):
#     return arg.split()

# if __name__ == "__main__":
#     HBNBCommand().cmdloop()