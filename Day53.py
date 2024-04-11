# Day 53 of 100 days of coding challenge
# Program to count frequency of each character in the string
txt = input("Enter a string : ")
d = {}
for i in txt:
    if i.lower() not in d:
        d[i.lower()] = 1
    else:
        d[i.lower()] += 1

print("Frequency of each character in the string",txt,"is")
for i in d:
    print(i,"occurs",d[i.lower()],"times")

