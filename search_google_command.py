import sys #Imported to bring the files from 1 layer above
import os
from googlesearch import search

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from database2 import object_type

class google_search_command(object_type):

    def __init__(self, name = "search", list_of_objects = []):
        '''
        Initialize a new google search command
        '''
        database.__init__(self, list_of_objects, name)

    def execute(self, args = []):
        '''Searches google using a string command as a query and prints a number of
        search results as links   
        '''
        keywords = ["who", "what", "when", "where", "why", "how"]
        index = 0
        query = ""

        #Narrows down which part is the search
        for i in range(0, len(args - 1)):
            #Conditions it searches for is "search" and the keywords above.
                #First condtion, takes everything after search and adds spaces to make it readable by google
                if args[i] == "search":
                    for j in range(i + 1, len(args - 1)):
                        query += args[j] + " "
                        
                    break #Implement grabbing everything in a second, use a for loop?
                elif args[i] in keywords:
                    for j in range(i, len(args - 1):
                        query += args[j] + " "
                    break
                       
        

        #for loop to print the amount of links in the query, limited to a number
        for j in search(query, tld="co.in", num = 10, stop = 10, pause = 2):
            print(j) #Just give results for now. Expand on this later?
