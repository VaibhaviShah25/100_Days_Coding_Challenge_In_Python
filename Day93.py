# Day 93 of 100 days of coding challenge
# Program to overload relational operators

class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def __str__(self):
        return "(Length {0}, Breadth {1})".format(self.l,self.b)

    def __gt__(self,other):
        if self.l * self.b > other.l * other.b:
            return True
        else:
            return False

r1 = Rectangle(10,12)
r2 = Rectangle(12,17)

print("First rectangle is",r1)
print("Second rectangle is",r2)
if r1 > r2:
    print("First Rectangle is bigger in area")
else:
    print("Second rectangle is bigger in area")
