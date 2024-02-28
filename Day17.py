#Day 17 of 100 days of coding challenge
#Program to print the HCF of two numbers
#Approach 1
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
a =  num1
b = num2
while num1 % num2 != 0:
    rem = num1 % num2
    num1 = num2
    num2 = rem
print("HCF of",a,"and",b,"is",num2)


