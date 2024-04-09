# Day 44 of 100 days of coding challenge
# Program to check if a string is palindrome or not without using any built-in function
a = input("Enter a string : ")
for i in range(len(a)//2):
    if a[i] == a[len(a)-1-i]:
        continue
    else:
        print("The string is not a palindrome")
        break
else:
    print("The string is a palindrome")
