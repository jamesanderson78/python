# Helpful websites for traubleshooting Python/Oracle connection
# http://www.golden-orb.ltd.uk/working-with-oracle-from-python-on-a-mac/
# https://github.com/kubo/fix_oralib_osx
import os
# Need to install cx_Oracle by running the following at the terminal:
# pip install cx_Oracle
import cx_Oracle
import csv
 
SQL="SELECT 'mySuccess' FROM dual"

 
# # You can set these in system variables but just in case you didnt
# os.putenv('ORACLE_HOME', '/oracle/product/10.2.0/db_1') 
# os.putenv('LD_LIBRARY_PATH', '/oracle/product/10.2.0/db_1/lib') 

# Use TNSNAMES.ORA for database connection
connection = cx_Oracle.connect('CMSTRACK', 'password', 'APPDBTST.WORLD')
 
cursor = connection.cursor()
cursor.execute(SQL)
for row in cursor:
#     output.writerow(row)
    print 'Here is the row of data from the database: '
    print row
cursor.close()
connection.close()
# FILE.close()

