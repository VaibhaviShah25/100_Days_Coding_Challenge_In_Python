#Day3 of 100 Days Coding Challenge
#Creating Student Report Card
name = input("Enter student name : ")
s1 = int(input("Enter your marks in subject 1: "))
s2 = int(input("Enter your marks in subject 2: "))
s3 = int(input("Enter your marks in subject 3: "))
s4 = int(input("Enter your marks in subject 4: "))
s5 = int(input("Enter your marks in subject 5: "))
total = s1 + s2 + s3 + s4 + s5
per = total / 500 * 100
print("--"*25)
print("\t\t\tREPORT CARD")
print("--"*25)
print("Name of the Student : ",name)
print("Total Marks of the student : ",total)
print("Percentage obtained by student : ",round(per,2))
if per >= 40:
    print("Congratulations!",name,"You have passed the exam")
else:
    print("Better Luck Next Time")
print("--"*25)

