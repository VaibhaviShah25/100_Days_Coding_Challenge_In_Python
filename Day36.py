# Day 36 of 100 days of coding challenge in Python
# Program to reverse a list
num = eval(input("Enter a list of numbers : "))
for i in range(len(num)//2):
    # Swapping corresponding positions from left and right
    num[i],num[len(num)-1-i] = num[len(num)-1-i],num[i]
print(num)

