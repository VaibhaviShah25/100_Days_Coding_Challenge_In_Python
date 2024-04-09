#Day 13 of 100 days coding challenge
#Program to find factors of a number
num = int(input("Enter a number : "))
print("Factors of the number are : ")
for i in range(1,num+1):
    if num % i == 0:
        print(i)

