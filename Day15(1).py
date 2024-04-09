#Day 15 of 100 days coding challenge
#Program to print the prime numbers in given range
start = int(input("Enter starting range : "))
end = int(input("Enter ending range : "))
print("Prime numbers in the range are:")
for i in range(start,end+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        if i != 1:
            print(i)

