# Day 28 of 100 days of coding challenge in Python
# Program to print patterns
n = int(input("Enter number of rows : "))
for i in range(0,n):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
