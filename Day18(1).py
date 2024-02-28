#Day 18 of 100 days of coding challenge
#Program to print the Fibonacci Series till nth number
n = int(input("Enter the highest number in Fibonacci Series : "))
a = 0
b = 1
c = a + b
print(a,b,end=" ")
while c <= n:
    print(c,end=" ")
    a = b
    b = c
    c = a + b
