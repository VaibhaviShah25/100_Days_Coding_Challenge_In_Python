# Day 62 of 100 days of coding challenge
# Program to read a text file line by line and display each word separated by a #
f = open("story.txt")
data = f.readlines()
for line in data:
    print("#".join(line.split()))


