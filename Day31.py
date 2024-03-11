# Day 31 of 100 days of coding challenge in Python
# Program to print patterns
n = int(input("Enter number of rows : "))
d = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j or i + j == n + 1 or i == 1 or i == n or j == 1 or j == n:
            print("*",end="")
        else:
            print(" ",end="")
    print()

