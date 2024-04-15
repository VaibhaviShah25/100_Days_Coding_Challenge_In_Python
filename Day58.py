# Day 58 of 100 days of coding challenge
# Program to validate phone number

def validatePhnumber(num):
    if num.isdigit() and len(num) == 10:
        if num[0] in '789':
            return True
        else:
            return False
    else:
        return False


num = input("Enter a phone number : ")
if validatePhnumber(num):
    print("Valid Phone number ")
else:
    print("Invalid phone number ")


