#!/usr/bin/python3

import MySQLdb
db = MySQLdb.connect(host="localhost",user="harv",passwd="password",db="travelexperts")
cursor = db.cursor()



try:
   # Execute the SQL command
   cursor.execute("SELECT * from agents")
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
       agentid = row[0]
       fname = row[1]
       lname = row[3]
       phone = row[4]
       email = row[5]
       # Now print fetched result
       print("id=%s, fname=%s, lname=%s, phone=%s, email=%s" % (agentid, fname, lname, phone, email ))
      
except:
   print("Error: unable to fecth data")


db.close()
