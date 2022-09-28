import comparison_transcriber as ct
import os
import sys

def _open_executable(file_name): #Will search for a file in the future. NEEDS TO BE FIXED. NOT CURRENTLY WORKING
    '''Opens executable type files. Needs a file name (currently a file directory) as a string

    '''

    os.system(file_name)



def _execute_command(command):
    run(command)
