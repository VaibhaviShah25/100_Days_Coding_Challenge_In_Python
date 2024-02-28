# Day 20 of 100 days of coding challenge
# Program to print palindrome of a number
n = int(input("Enter a number : "))
res = 0
a = n
while n > 0:
    d = n % 10
    res = res * 10 + d
    n //= 10
print("Reverse of",a,"is",res)
if res == a:
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")

