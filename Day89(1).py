# Day 89 of 100 days of coding challenge
# Working with multilevel inheritance
class Circle:
    def __init__(self,r):
        self.r = r
    def display(self):
        print("Radius is",self.r)
        area = 3.14 * self.r * self.r
        print("Area is",area)

class Cylinder(Circle):
    def __init__(self,r,h):
        super().__init__(r)
        self.h = h
    def displayVol(self):
        super().display()
        print("Height is",self.h)

class Cone(Cylinder):
    def __init__(self,r,h,lh):
        super().__init__(r,h)
        self.lh = lh
    def displayConeVol(self):
        super().displayVol()
        print("Lateral height is",self.lh)

cn = Cone(7,12,10)
cn.displayConeVol()