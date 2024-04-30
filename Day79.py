# Day 79 of 100 days of coding challenge
# Program to shift numbers in a list to left by n times

def LShift(a,n):
    for i in range(n):
        c = a.pop(0)
        a.append(c)
    return a


a = eval(input("Enter a list of numbers : "))
n = int(input("Enter the value of n to be shifted : "))
print(LShift(a,n))

