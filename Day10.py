#Day 10 of 100 days coding challenge
#Program to calculate profit or loss
cp = float(input("Enter cost price of product : "))
sp = float(input("Enter selling price of product : "))

if sp > cp:
    print("Profit is Rs.",sp-cp)
elif cp > sp:
    print("Loss is Rs.",cp-sp)
else:
    print("No profit No loss")
