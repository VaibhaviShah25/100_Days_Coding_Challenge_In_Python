# Day 29 of 100 days of coding challenge in Python
# Program to print patterns
n = int(input("Enter number of rows : "))
for i in range(n):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
for l in range(n-1,0,-1):
    for p in range(n,l-1,-1):
        print(" ",end="")
    for m in range(2*l-1,0,-1):
        print("*",end="")
    print()

