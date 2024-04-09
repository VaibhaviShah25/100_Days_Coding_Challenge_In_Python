# Day 46 of 100 days of coding challenge
# Program to reverse a string word without using in-built function
a = input("Enter a string : ")
b = ""
for i in range(len(a)-1,-1,-1):
    b += a[i]
print("String before reverse :",a)
print("String after reverse :",b)
