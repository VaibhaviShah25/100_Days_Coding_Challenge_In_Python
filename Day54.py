# Day 54 of 100 days of coding challenge
# Program to change string in toggle case
txt = input("Enter a string : ")
print("Th Original String is",txt)
print("String in Toggle case is ",end="")
for i in txt:
    if i.islower():
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")

