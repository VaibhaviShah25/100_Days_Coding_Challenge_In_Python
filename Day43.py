# Day 43 of 100 days of coding challenge
# Program for insertion sort
num = eval(input("Enter a list of numbers : "))
for i in range(1,len(num)):
    a = num[i]
    j = i-1
    while j >= 0 and a < num[j]:
        num[j+1] = num[j]
        j -= 1
    num[j+1] = a

print("List after sorting is ",num)
