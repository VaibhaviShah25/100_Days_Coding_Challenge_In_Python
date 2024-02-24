#Day 14 of 100 days coding challenge
#Program to check if a number is perfect number or not
num = int(input("Enter a number : "))
p = 0
for i in range(1,num):
    if num % i == 0:
        p += i
if p == num:
    print("It is a perfect number ")
else:
    print("It is not a perfect number")

