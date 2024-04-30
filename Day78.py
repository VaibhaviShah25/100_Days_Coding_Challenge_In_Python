# Day 78 of 100 days of coding challenge
# Program to check if a number is automorphic number or not

def isautomorphic_num(num):
    sq = num ** 2
    p = len(str(num))
    if str(sq)[-p:] == str(num):
        return True
    else:
        return False


num = int(input("Enter a number : "))
if isautomorphic_num(num):
    print(num,"is an automorphic number ")
else:
    print(num,"is not an automorphic number ")

ll = int(input("Enter lower limit : "))
ul = int(input("Enter upper limit : "))
c = 0
print("automorphic numbers in the range are :")

for i in range(ll,ul+1):
    if isautomorphic_num(i):
        c += 1
        print(i)
if c == 0:
    print("No automorphic numbers in given range")

