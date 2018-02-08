#!/usr/bin/env python
#* 
#* Ver 0.3
#* For python version 2.7 script dump all databases
#*
#
import MySQLdb
import string
import subprocess
import re
import os
import sys
import datetime

#
# variables for connect to MySQL
# ( command example: ./mysql_dump.py "localhost" "user" "password" )
#
HOST = sys.argv[1]
USER = sys.argv[2]
PASSWD = sys.argv[3]

#
# function return results of execute with MySQL
#
def mysql(param,DATABASE = ""):
    db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DATABASE)
    cursor = db.cursor()
    cursor.execute(param)
    return cursor.fetchall()

#
ALL_DATABASES = mysql("SHOW DATABASES")

#
# Get datetime
#
today = datetime.datetime.today()

#
# output on display all databases, tables and create dumpsql
#
print "******* List all database and tables *******"
print("Created: "+today.strftime("%Y-%m-%d %H:%M") ) # print date
print
for basename in ALL_DATABASES:
     basename = re.sub("[)(',]","",str(basename)) # the brackets are deleted from basename
     if not os.path.exists(basename):
        os.mkdir(basename) # create the directory
     print "BASE_NAME: '"+basename+"'"
     ALL_TABLES = mysql("SHOW TABLES",basename)
     print "--- ALL_TABLE_NAME: ---"
     for table in ALL_TABLES:
        print "    "+re.sub("[)(',]","",str(table)) # the brackets are deleted from ALL_TABLES
     print
     # create dump
     subprocess.call("mysqldump --ignore-table=mysql.event --skip-opt -h"+HOST+" -u"+USER+" -p"+PASSWD+" "+basename+" > "+basename+"/"+basename+".sql", shell=True)

print "**********************************************"
print

#
#
#






