# Helpful websites for traubleshooting Python/Oracle connection
# http://www.golden-orb.ltd.uk/working-with-oracle-from-python-on-a-mac/
# https://github.com/kubo/fix_oralib_osx
import os
# Need to install cx_Oracle by running the following at the terminal:
# pip install cx_Oracle
import cx_Oracle
import csv
import json
 
# SQL="SELECT 'mySuccess' FROM dual"
SQL="SELECT * FROM developer"

# Open file
with open ("/Users/jamesanderson/Documents/properties.json", "r") as myfile:
    data = myfile.read()
    
# Parse the file as JSON data
theJSON = json.loads(data)

# Use TNSNAMES.ORA for database connection
connection = cx_Oracle.connect(theJSON["databases"]["APUSDEV"]["username"], 
                                theJSON["databases"]["APUSDEV"]["password"], 
                                theJSON["databases"]["APUSDEV"]["tnsname"])
 
# # Implement the Oracle connection with WALLET instead of username/password
# # http://stackoverflow.com/questions/10485145/authentication-with-public-keys-and-cx-oracle-using-python
# connection = cx_Oracle.connect("/@ORCL_MY_USER")
  
cursor = connection.cursor()
cursor.execute(SQL)
for row in cursor:
#     output.writerow(row)
    print 'Here is the row of data from the database: '
    print row
cursor.close()
connection.close()



