#Day 6 of 100 days coding challenge
#Program to calculate electricity bill
print("-"*40)
print("\t\tELECTRICITY BILL")
print("-"*40)
units = int(input("Enter number of units consumed : "))
if units < 200:
    bill = units * 4
elif units < 500:
    bill = 800 + (units-200) * 6
elif units < 800:
    bill = 800 + 1800 + (units-500) * 8
else:
    bill = 800 + 1800 + 2400 + (units-800) * 10
print("Electricity bill -->",bill)
print("-"*40)

