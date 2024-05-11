# Day 89 of 100 days of coding challenge
# Working with multilevel inheritance
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name is",self.name)
        print("Age is",self.age)

class Student(Person):
    def __init__(self,name,age,dob):
        self.dob = dob
        super().__init__(name,age) # inheriting Person class
    def Displaydata(self):
        super().display()
        print("Date of birth is",self.dob)

class Employee(Student):
    def __init__(self,name,age,dob,stipend):
        self.stipend = stipend
        super().__init__(name,age,dob)
    def displayInfo(self):
        super().Displaydata()
        print("Stipend is Rs.",self.stipend)

a = Employee("Rahul",22,"23-12-2002",30000)
a.displayInfo()
