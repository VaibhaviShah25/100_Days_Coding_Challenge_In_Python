# Day 37 of 100 days of coding challenge in Python
# Program to swap adjacent elements
num = eval(input("Enter a list of numbers : "))
for i in range(0,len(num)-2,2):
    # Swapping corresponding positions from left and right
    num[i],num[i+1] = num[i+1],num[i]
print(num)
