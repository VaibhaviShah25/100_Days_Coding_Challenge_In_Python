''' Day 49 of 100 days of coding challenge
Program to rotate a list from it's left without using any built-in methods
and functions on lists '''
num = eval(input("Enter a list of numbers : "))
k = int(input("Enter the number of elements to be shifted : "))
print("List before rotation is",num)
for i in range(k):
    temp = num[0]
    for j in range(len(num)-1):
        num[j] = num[j+1]
    num[-1] = temp

print("List after shifting is",num)
