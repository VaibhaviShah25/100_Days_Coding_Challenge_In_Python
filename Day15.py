#Day 15 of 100 days coding challenge
#Program to check if a number is prime number or not
num = int(input("Enter a number : "))
for i in range(2,num):
    if num % i == 0:
        print("It is not a prime number")
        break
else:
    print("It is a prime number")
