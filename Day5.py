#Day 5 of 100 days coding challenge
#Program to calculate the roots of quadratic equation
import math
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
d = b ** 2 - 4 * a * c
if d < 0:
    print("No real roots")
elif d == 0:
    r1 = r2 = -b / (2 * a)
    print("Real and equal roots are",r1,r2)
else:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print("Real and Unequal roots are",r1,r2)
