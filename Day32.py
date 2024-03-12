# Day 32 of 100 days of coding challenge in Python
# Program for a dice game
import random
import time
name1 = input("Enter name of Player 1 : ")
name2 = input("Enter name of Player 2 : ")
print(name1,"throwing dice",end="")
for i in range(3):
    print(".",end = "")
    time.sleep(1)
val1 = random.randint(1,6)
print("\n",name1,"got",val1)
print(name2,"throwing dice",end="")
for i in range(3):
    print(".",end = "")
    time.sleep(1)
val2 = random.randint(1,6)
print("\n",name2,"got",val2)
if val1 > val2:
    print(name1,"wins!")
elif val1 < val2:
    print(name2,"wins!")
else:
    print("There is a DRAW!")
