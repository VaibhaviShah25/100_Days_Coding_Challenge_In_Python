# Day 75 of 100 days of coding challenge
# Program to search a record using MySQL and Python

import mysql.connector   # Establishing connection
con = mysql.connector.connect(host="localhost",user="root",password="",database="college")
if con.is_connected():
    adm_id = int(input("Enter admission number of the student to be searched : "))
    q = "select * from student where adm_id="+str(adm_id)
    cur = con.cursor()
    cur.execute(q)
    res = cur.fetchone()
    if res != None:
        print("Found")
        print(res)
    else:
        print("No student found with given ID")
else:
    print("Error in connection")

