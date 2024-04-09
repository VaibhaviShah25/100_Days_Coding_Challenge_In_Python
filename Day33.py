# Day 33 of 100 days of coding challenge in Python
# CLI based Guess the Number Game
import random
print("*"*40)
print("  WELCOME TO GUESS THE NUMBER GAME")
print("*"*40)
name = input("Enter Player Name : ")
num = random.randint(1,100)
print("Guess any number between 1 and 100")
for i in range(5):
    guess = int(input("Enter your guess : "))
    if guess == num:
        print("Congratulations!",name,"wins")
        break
    elif guess > num:
        print("The number is smaller than your guess")
    else:
        print("The number is greater than your guess")
else:
    print("Ohh! Better Luck Next Time")

