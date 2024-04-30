# Day 73 of 100 days of coding challenge
# Program to update a record using MySQL and Python

import mysql.connector   # Establishing connection
con = mysql.connector.connect(host="localhost",user="root",password="",database="college")
if con.is_connected():
    adm_id = int(input("Enter admission number : "))
    dob = input("Enter new date of birth (YYYY-MM-DD): ")
    q = "update student set dob=%s where Adm_Id=%s"  # query
    values = (dob,adm_id)
    cur = con.cursor()  # forming cursor
    cur.execute(q, values)
    con.commit()
    print("Student updated successfully")

else:
    print("Error in connection")

