#Day 19 of 100 days of coding challenge
#Program to print sum of digits of a number
n = int(input("Enter a number : "))
s = 0
while n > 0:
    d = n % 10
    s += d
    n //= 10
print("Sum of digits is",s)

