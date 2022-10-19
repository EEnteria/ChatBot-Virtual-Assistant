import sys #Imported to bring the files from 1 layer above
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from database2 import object_type

class find_command(object_type):
     def __init__(self, file_name):
          self._file_name  = file_name

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
                         break #Made to find the first file at the moment
            

        #Old deprecated code
        #if file_name in files:
            #os.system(file_name)
            #print("FILE FOUND")
        #else:
            #print("nothing")
