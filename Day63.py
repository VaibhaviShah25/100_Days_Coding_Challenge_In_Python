# Day 63 of 100 days of coding challenge
# Program to create login screen using CSV Files
import csv
uname = input("Enter username : ")
passw = input("Enter password : ")
f = open("users.csv","r")
data = csv.reader(f)
for ch in data:
    if ch[0] == uname and ch[1] == passw:
        print("Welcome",uname,"Access granted")
        break
else:
    print("Invalid username or password ")
f.close()

