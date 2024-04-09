# Day 45 of 100 days of coding challenge
# Program to count number of vowels in a string
a = input("Enter a string : ")
cnt = 0
for i in range(len(a)):
    if a[i] in 'AEIOUaeiou':
        cnt += 1
print("Number of vowels in string is",cnt)
