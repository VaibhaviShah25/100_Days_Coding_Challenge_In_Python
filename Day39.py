# Day 39 of 100 days of coding challenge in Python
# Program to delete duplicates from a list
num = eval(input("Enter a list of numbers : "))
i = 0
while i < len(num):
    if(num.count(num[i])) > 1:
        num.remove(num[i])
    else:
        i += 1
print("List after removing duplicates is : ",num)
