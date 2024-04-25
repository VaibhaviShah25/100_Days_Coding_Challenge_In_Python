# Day 71 of 100 days of coding challenge
# Program for showing Table Data using MySQL and Python
import mysql.connector   # Establishing connection
con = mysql.connector.connect(host="localhost",user="root",password="",database="college")
if con.is_connected():
    q = "select * from student"
    cur = con.cursor()   # forming cursor
    cur.execute(q)
    res = cur.fetchall()
    for row in res:
        print("Adm Id is",row[0],"Name is",row[1],"Dob is",row[2])
    if cur.rowcount == 0:
        print("Table is empty")
    else:
        print(cur.rowcount," students processed")

else:
    print("Error in connection")


