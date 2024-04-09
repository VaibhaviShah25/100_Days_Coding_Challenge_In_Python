# Day 42 of 100 days of coding challenge in Python
# Program for bubble sort
num = eval(input("Enter a list of numbers : "))
for i in range(len(num)):
    for j in range(len(num)-1-i):
        if num[j] > num[j+1]:
            num[j],num[j+1] = num[j+1],num[j]

print("The sorted list is",num)

