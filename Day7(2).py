#Day 7 of 100 days coding challenge
#Program to print leap year between a given range
st_year = int(input("Enter starting year : "))
end_year = int(input("Enter ending year : "))
print("Leap year in the range are : ")
for year in range(st_year,end_year+1):
    if year % 100 == 0:
        if year % 400 == 0:
            print(year)
    elif year % 4 == 0:
        print(year)



