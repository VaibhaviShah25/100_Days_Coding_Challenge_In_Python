# Day 23 of 100 days of coding challenge in Python
# Program to print the sum of series x + x^2/2! + x^3/3! +...
x = int(input("Enter the number : "))
n = int(input("Enter maximum power to be raised : "))
s = 0
p = 1
for i in range(1,n+1):
    p *= i
    s += x ** i / p
print("The sum of series is",round(s,3))



