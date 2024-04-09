# Day 41 of 100 days of coding challenge
# Program of selection sort
num = eval(input("Enter a list of numbers : "))
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i] > num[j]:
            num[i],num[j] = num[j],num[i]

print("The sorted list is",num)

