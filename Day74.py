# Day 74 of 100 days of coding challenge
# Program to delete a record using MySQL and Python

import mysql.connector   # Establishing connection
con = mysql.connector.connect(host="localhost",user="root",password="",database="college")
if con.is_connected():
    adm_id = int(input("Enter admission number of the student to be deleted : "))
    cur = con.cursor() # forming cursor
    q = "select * from student"
    cur.execute(q)
    res = cur.fetchall()
    for row in res:
        if row[0] == adm_id:
            print("Student record to be deleted : \nAdm_Id is",row[0],"Name is",row[1],"Dob is",row[2])
            break
    q = "delete from student where adm_id=%s"  # query
    values = (adm_id,)
    cur.execute(q, values)
    con.commit()
    print("Student deleted successfully")
else:
    print("Error in connection")



