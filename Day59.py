# Day 59 of 100 days of coding challenge
# Program to check strength of a password
password = input("Enter the required password : ")
n = len(password)
if n >= 8 and n <= 16:
    c = 0
    s = 0
    d = 0
    sp = 0
    a = 0
    for ch in password:
        if ch.isupper():
            c += 1
        elif ch.islower():
            s += 1
        elif ch.isdigit():
            d += 1
        elif ch in '.,;:@#$%^&*(){}<>':
            sp += 1
        else:
            a += 1

    if a != 0:
        print("Invalid password ")
    else:
        if c > 0 and s > 0 and d > 0 and sp > 0:
            print("Strong password ")
        else:
            print("Weak password ")
else:
    print("Password can have minimum of 8 characters and maximum 16")

