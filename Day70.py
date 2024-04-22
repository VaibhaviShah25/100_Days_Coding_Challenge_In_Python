# Day 70 of 100 days of coding challenge
# Program to print sum of digits of a number using recursion

def sumofdigits(num):
    if num == 0:
        return 0
    res = num % 10 + sumofdigits(num//10)
    return res

n = int(input("Enter a number : "))
res = sumofdigits(n)
print("Sum of digits of",n,"is",res)

