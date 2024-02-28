# Day 21 of 100 days of coding challenge
# Program to print sum of series 1 + 1/2 + 1/3 + 1/4 +...
n = int(input("Enter a number : "))
s = 0
for i in range(1,n+1):
    s += 1 / i
    if i < n:
        print("1/"+str(i)+" + ",end="")

    else:
        print("1/"+str(i)+" = "+str(round(s,3)))

