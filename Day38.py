# Day 38 of 100 days of coding challenge in Python
# Program to swap first half of the list to second half
num = eval(input("Enter a list of numbers : "))
if len(num) % 2 == 0:
    n = len(num)//2
else:
    n = len(num)//2 + 1
for i in range(len(num)//2):
    num[i],num[i+n] = num[i+n],num[i]
print(num)
