import comparison_transcriber as ct
import os
import sys
from googlesearch import search

def _open_executable(file_name): #Will search for a file in the future. NEEDS TO BE FIXED. NOT CURRENTLY WORKING
    '''Opens executable type files. Needs a file name (currently a file directory) as a string

    '''

    os.system(file_name)


def _execute_command(command):
    '''
    This can be used for date and time as well
    or for any simple command. Can be easily connected to
    the library
    '''
    command = command.lower()
    run(command)


def search_google(command):
    '''Searches google using a string command as a query and prints a number of
    search results as links
        
    '''
    query = command

    #for loop to print the amount of links in the query, limited to a number
    for j in search(query, tld="co.in", num = 10, stop = 10, pause = 2):
        print(j)


    
def create_file(filename, text):
    '''
    Takes a filename and text to put it into.
    '''


def create_appointments(filename, text):
    '''
    Randomize file names? put them into a common folder
    '''

def read_appointments():
    '''
    need to find a way to iterate through a folder full of files and read them out.
    '''
