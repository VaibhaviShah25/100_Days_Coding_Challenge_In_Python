# Day 25 of 100 days of coding challenge
# Program to print Armstrong numbers in the given range
start = int(input("Enter starting range : "))
end = int(input("Enter ending range : "))
for i in range(start,end+1):
    digits = 0
    num = num2 = i
    s = 0
    while num > 0:
        num //= 10
        digits += 1
    for j in range(digits):
        d = num2 % 10
        s += d ** digits
        num2 //= 10
    if s == i:
        print(i)
    else:
        continue
