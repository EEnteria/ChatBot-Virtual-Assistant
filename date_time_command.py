import sys #Imported to bring the files from 1 layer above
from database2 import object_type
from datetime import datetime

#Date-time works

class date_time_command(object_type):
    '''
        Database Directly Accesses this object of this class
    '''

    def __init__(self, name = "date", list_of_objects = []): #Init is here to give a default value. Helps w/ redundancy and incorrect values

        database.__init__(self, list_of_objects, name)
    
    def execute(self, args = []):
        '''
            Gives the current system date and time, as simple as that
        '''
    #Args refers to leftover commands, not needed here
    
        time = datetime.now().time()
        date = datetime.now().date()

        print("Time:", time)
        print("Date", date)
