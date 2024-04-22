# Day 69 of 100 days of coding challenge
# Program to find HCF of 2 numbers using recursion
def HCF(n1,n2):
    if n1 % n2 == 0:
        return n2
    else:
        res = HCF(n2,n1%n2)
        return res


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
res = HCF(a,b)
print("HCF of",a,"and",b,"is",res)
