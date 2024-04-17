# Day 61 of 100 days of coding challenge
# Program to count vowels in a csv file
'''
f = open("story.txt","w")
f.write("Hello! This is a sample file which we are creating using Python Program\n")
f.write("This file will be used through other program to read content of this file and print it.\nThank you!")'''

f = open("story.txt","r")
data = f.read()
vowel = 0
print(data)
for ch in data:
    if ch in 'aeiouAEIOU':
        vowel += 1

print("No. of vowels are",vowel)

