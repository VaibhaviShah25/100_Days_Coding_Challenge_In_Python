# Day 72 of 100 days of coding challenge
# Program to insert data into a table using MySQL and Python

import mysql.connector   # Establishing connection
con = mysql.connector.connect(host="localhost",user="root",password="",database="college")
if con.is_connected():
    admno = int(input("Enter admission number : "))
    name  = input("Enter name of the student : ")
    dob = input("Enter Date of birth (YYYY-MM-DD): ")
    q = "insert into student values(%s,%s,%s)"   # query
    values = (admno,name,dob)
    cur = con.cursor()   # forming cursor
    cur.execute(q,values)
    con.commit()
    print("Student inserted successfully")

else:
    print("Error in connection")


