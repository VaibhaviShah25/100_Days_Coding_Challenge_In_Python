# Day 34 of 100 days of coding challenge in Python.
# Code to implement Linear Search
num = eval(input("Enter a list of numbers : "))
n = eval(input("Enter the number to be searched : "))
c = 0
for i in range(len(num)):
    if num[i] == n:
        print("Number found at",i+1)
        c += 1
if c == 0:
    print("Number not found")

