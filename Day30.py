# Day 30 of 100 days of coding challenge in Python
# Program to print patterns
n = int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*",end="")
    for k in range(2*i-2):
        print(" ",end="")
    for a in range(i-1,n):
        print("*",end="")
    print()
for i in range(n,0,-1):
    for a in range(i-1,n):
        print("*",end="")
    for k in range(2*i-2):
        print(" ",end="")
    for j in range(n,i-1,-1):
        print("*",end="")
    print()
