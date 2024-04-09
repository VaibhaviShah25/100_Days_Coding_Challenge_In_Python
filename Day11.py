#Day 11 of 100 days coding challenge
#Program to print multiplication table of a number
num = int(input("Enter a number : "))
print("Multiplication table of",num,":")
for i in range(1,11):
    print(num,"X",i,"=",num*i)
