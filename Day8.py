#Day 8 of 100 days coding challenge
#Program to check if a triangle is equilateral, isosceles, scalene
s1 = float(input("Enter side 1 of triangle : "))
s2 = float(input("Enter side 2 of triangle : "))
s3 = float(input("Enter side 3 of triangle : "))
if s1 == s2 == s3:
    print("Triangle is Equilateral triangle")
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("Triangle is Isosceles triangle")
else:
    print("Triangle is Scalene triangle")
