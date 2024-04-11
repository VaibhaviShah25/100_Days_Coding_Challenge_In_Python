# Day 47 of 100 days of coding challenge
# Program to print Intersection and Union of two lists
n1 = eval(input("Enter list 1 : "))
n2 = eval(input("Enter list 2 : "))
print(n1)
print(n2)
intersect = []
union = []
for i in n1:
    if i in n2 and i not in intersect:
        intersect.append(i)
    union.append(i)
print("Intersection of the two list is",intersect)
for j in n2:
    if j not in union:
        union.append(j)

print("Union of the two list is",union)

