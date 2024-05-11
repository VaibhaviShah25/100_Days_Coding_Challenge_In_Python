# Day 88 of 100 days of coding challenge in Python
# Program to implement single level inheritance in rectangle class

class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def display(self):
        print('Length is',self.l)
        print('Breadth is',self.b)
    def Area(self):
        print('Area is',self.l * self.b)

class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        self.h = h
        super().__init__(l,b)

    def displayInfo(self):
        super().display()
        print('Height is',self.h)

    def Volume(self):
        print('Volume is',self.l * self.b * self.h)

obj = Cuboid(10,12,13)
obj.displayInfo()
obj.Volume()


