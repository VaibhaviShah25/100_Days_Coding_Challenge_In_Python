#Day 9 of 100 days coding challenge
#Program to print the grade of student according to percentage marks
per = float(input("Enter percentage marks secured : "))
if per >= 90:
    print("Grade is A+")
elif per >= 80:
    print("Grade is A")
elif per >= 60:
    print("Grade is B")
elif per >= 50:
    print("Grade is C")
else:
    print("Grade is D")


