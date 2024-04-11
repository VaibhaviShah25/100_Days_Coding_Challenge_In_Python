# Day 48 of 100 days of coding challenge
# Program to print Cartesian Product of two lists
n1 = eval(input("Enter list 1 : "))
n2 = eval(input("Enter list 2 : "))
pro = []
for i in n1:
    for j in n2:
        pro.append((i,j))

print("Cartesian Product is",pro)
