#Day 18 of 100 days of coding challenge
#Program to print the Fibonacci Series
n = int(input("Enter how many elements in Fibonacci Series to be printed : "))
a = 0
b = 1
print(a,b,end=" ")
for i in range(n-2):
    c = a + b
    print(c,end = " ")
    a = b
    b = c

