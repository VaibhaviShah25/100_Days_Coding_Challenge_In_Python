# Day 86 of 100 days of coding challenge
# Program to create Student class

class Student: # Creating class student
    def __init__(self,rno=0,nm="not defined",mk=0):
        self.rollno = rno
        self.name = nm
        self.marks = mk


    def result(self):
        if self.marks >= 40:
            print(self.name + " is Pass")
        else:
            print(self.name + " is Fail")


rno = int(input("Enter rollno of the student : "))
name = input("Enter name of the student : ")
marks = int(input("Enter marks of the student : "))
s1 = Student(rno,name,marks)
(s1.result())
s2 = Student()
s2.result()

