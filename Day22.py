# Day 22 of 100 days coding challenge
# Program to print sum of series : x + x^2 + x^3 + x^4 + ...
x = int(input("Enter base number : "))
n = int(input("Enter power number :  "))
s = 0
for i in range(1,n+1):
    s += x ** i
    if i < n:
        print(str(x)+"^"+str(i)+" + ",end="")
    else:
        print(str(x)+"^"+str(i)+" = "+str(s))
