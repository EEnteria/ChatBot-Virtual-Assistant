import sys #Imported to bring the files from 1 layer above
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from database2 import object_type

class command_command(object_type): #NEEDS TO BE INITIALIZED AND TESTED
    def __init__(self, command):
        self.command = command

    def execute_command_():
        self.command = self.command.lower()
        os.system(self.command)
                
