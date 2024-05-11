# Day 91 of 100 days of coding challenge
# Working with multiple inheritance
class Address:
    def displaya(self):
        print("Address is OK")

class PhoneNum:
    def displayph(self):
        print("Phone number is: 9421858668")


class Person(Address,PhoneNum):   # inheriting multiple classes
    def display(self):
        print("Name is: OKOK")
        Address.displaya(self)
        PhoneNum.displayph(self)

nm = Person()
nm.display()

# nm.displayph()
# nm.displaya()
