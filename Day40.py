# Day 40 of 100 days of coding challenge in Python
# Program to find second highest number from a list
num = eval(input("Enter a list of numbers : "))
max = num[0]
sec_highest = num[0]
for i in num:
    if i > max:
        max = i
for i in num:
    if i >= sec_highest and i != max:
        sec_highest = i

print("The second highest number in the List is",sec_highest)
