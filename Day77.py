# Day 77 of 100 days of coding challenge
# Program to check if a number is strong number or not
def factorial(num):
    if num == 0 or num == 1:
        return 1
    fact = num * factorial(num-1)
    return fact

def isstrong_number(n):
    num = n
    c = 0
    while n > 0:
        d = n % 10
        f = factorial(d)
        n //= 10
        c += f
    if num == c:
        return True
    else:
        return False


number = int(input("Enter a number : "))
if isstrong_number(number):
    print(number,"is a strong number ")
else:
    print(number,"is not strong number ")

