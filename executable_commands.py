import comparison_transcriber as ct
import os
import sys
import win32api
import re
from ics import Calendar, Event
from googlesearch import search
from datetime import datetime



def find(file_name):
    '''
        Finds a specific file within your computer.
    '''
    #Converts file name into a reguar expression
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split("\000")[:-1]:
        _find_file(drive, rex)

def _find_file(root_folder, rex): #Will search for a file in the future. NEEDS TO BE FIXED. NOT CURRENTLY WORKING
    '''
        Helper function for the one above, helps find files within every drive by iterating
        through every directory
        File name is used for the execution of .exe files, maybe hae a system to sort it out
    '''
    
    #find a way to search for something.
    #Use desktop shortcuts? DOES NOT WORK

    for root, dir, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            
            if result:
                print("FILE FOUND", os.path.join(root,f))
                os.system(f)
                break #Made to find the first one
            
                       
        #if file_name in files:
            #os.system(file_name)
            #print("FILE FOUND")
        #else:
            #print("nothing")

def _execute_command_(command):
    '''
    This can be used for date and time as well
    or for any simple command. Can be easily connected to
    the library DEPRECATED
    '''
    command = command.lower()
    os.system(command)
    

def _print_date_time():
    '''
        Gave up trying to make it read from commands above, easier to just use datetime
    '''
    
    time = datetime.now().time()
    date = datetime.now().date()

    print("Time:", time)
    print("Date", date)
    

def search_google(command):
    '''Searches google using a string command as a query and prints a number of
    search results as links
        
    '''
    query = command

    #for loop to print the amount of links in the query, limited to a number
    for j in search(query, tld="co.in", num = 10, stop = 10, pause = 2):
        print(j)


    
def create_file_txt(filename, text):
    '''
    Takes a filename and text to put it into it. Works with TXT files, experiment w/ word Files?
    '''
    new_File = (filename + ".txt")
    


def create_appointments(filename, start, end, calendar = None): #Might want to deal with descriptions
    event = Event(filename, start, end)
    

    if not calendar: #Checks for the instantiation of a calendar
        c = Calendar()

    else:
        c = calendar
        
    '''
    Randomize file names? put them into a common folder
    '''

def read_appointments():
    '''
    need to find a way to iterate through a folder full of files and read them out.
    '''


def _create_calendar(cal_name):
    
