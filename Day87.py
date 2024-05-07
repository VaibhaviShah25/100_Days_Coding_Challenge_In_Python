# Day 87 of 100 days of coding challenge
# Program to create constructors
class Triangle:
    def __init__(self,x=1,y=1,z=1):  # Forming constructor(Parameterized constructor)
        self.s1 = x
        self.s2 = y
        self.s3 = z

    def show(self):
        print("Side 1 is",self.s1)
        print("Side 2 is", self.s2)
        print("Side 3 is", self.s3)


print("Sides of triangle 1 : ")
t1 = Triangle(2,3,4)
t1.show()
print("Sides of triangle 2 : ")
t2 = Triangle()
t2.show()
