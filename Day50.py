# Day 50 of 100 days of coding challenge
# Program to print all combinations of three-digit number
a = [0,0,0]
a[0] = int(input("Enter first digit : "))
a[1] = int(input("Enter second digit : "))
a[2] = int(input("Enter third digit : "))
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                print(a[i],a[j],a[k])

