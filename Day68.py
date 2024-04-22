# Day 68 of 100 days of coding challenge
# Program to print factorial of a number using recursion

def factorial(num):
    if num == 1:
        return 1
    res = num * factorial(num-1)
    return res


n = int(input("Enter a number : "))
r = factorial(n)
print("Factorial of",n,"is",r)

