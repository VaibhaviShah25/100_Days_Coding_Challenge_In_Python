#Day 4 of 100 Days coding challenge
#Program to print the bill
name = input("Enter costumer name : ")
total = 0
dis = 0.0
products = int(input("Enter how many products are there : "))
for i in range(products):
    pr_name = input("Enter product name : ")
    cost = float(input("Enter cost of the product : "))
    qty = float(input("Enter quantity of the product : "))
    amount = cost * qty
    total += amount
gst = 12 * total / 100
total += gst
if total > 1000:
    dis = total * 5 / 100
elif total > 2000:
    dis = total * 10 / 100
elif total > 3000:
    dis = total * 20 / 100
print("--"*20)
print("\t\t\t\tBILL")
print("--"*20)
print("Total items -->",products)
print("GST applied 12% -->",gst)
print("Discount received -->",dis)
print("Amount Payable -->",total)
print("--"*20)
print("\t     THANKS FOR VISITING ")
print("--"*20)

