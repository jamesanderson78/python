#
# Example file for working with os.path module

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
  # Print the name of the OS
  print os.name
  
  # Check for item existence and type
  print "Item exists: " + str(path.exists("myfile.txt"))
  print "Item is a file: " + str(path.isfile("myfile.txt"))
  print "Item is a directory: " + str(path.isdir("myfile.txt"))
  
  # Work with file paths
  print "Item's path: " + str(path.realpath("myfile.txt"))
  print "Item's path and name: " + str(path.split(path.realpath("myfile.txt")))
  
  # Get the modification time
  t = time.ctime(path.getmtime("myfile.txt"))
  print t
  print datetime.datetime.fromtimestamp(path.getmtime("myfile.txt"))
  
  # Calculate how long ago the item was modified
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("myfile.txt"))
  print "It has been " + str(td) + "The file was modified"
  print "Or, " + str(td.total_seconds()) + " seconds"
  
if __name__ == "__main__":
  main()
