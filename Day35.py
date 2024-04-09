# Day 35 of 100 days of coding challenge in Python.
# Code to implement Binary Search
num = eval(input("Enter a list of numbers : "))
n = eval(input("Enter the number to be searched : "))
beg = 0
end = len(num) - 1
mid = (beg + end) // 2
while beg <= end:
    mid = (beg + end) // 2
    if num[mid] == n:
        print("Number found at",mid+1)
        break
    elif num[mid] < n:
        beg = mid + 1
    else:
        end = mid - 1
else:
    print("Number not found")

