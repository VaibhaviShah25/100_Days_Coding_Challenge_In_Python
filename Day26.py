# Day 26 of 100 days coding challenge in Python
# Program to print patterns
n = int(input("Enter number of rows : "))
def Pattern1(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def Pattern2(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()

def Pattern3(n):
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            print(j,end=" ")
        print()

def Pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

Pattern1(n)
print()
Pattern2(n)
print()
Pattern3(n)
print()
Pattern4(n)
