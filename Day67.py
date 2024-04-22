# Day 67 of 100 days of coding challenge
# Program to check if a word has easy pronunciation

word = input("Enter a word : ")
c = 0

for ch in word:
    if ch.isalpha():
        if ch not in 'aeiouAEIOU':
            c += 1
            if c == 4:
                print("It is difficult to pronounce")
                break
        else:
            c = 0
    else:
        print("Invalid Input")
        break
else:
    print("It is easy to pronounce")
