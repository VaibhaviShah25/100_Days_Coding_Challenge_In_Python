#Day 16 of 100 days of coding challenge
#Program to print the LCM of two numbers
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if num1 < num2:
    g1 = num1
    g2 = num2
else:
    g1 = num2
    g2 = num1
for i in range(g2,num1*num2+1):
    if i % g1 == 0 and i % g2 == 0:
        lcm = i
        break
print("LCM of",num1,"and",num2,"is",lcm)


