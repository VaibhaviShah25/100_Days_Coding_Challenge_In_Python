#Day 7 of 100 days coding challenge
#Program to check if the year entered is leap year or not
year = int(input("Enter Year : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    elif year % 4 == 0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
else:
    print(year,"is not a leap year")


