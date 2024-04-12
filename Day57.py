# Day 57 of 100 days of coding challenge
# Program to validate name entered by user
def validateName(name):
    for i in name:
        if i.isalpha() or i == " ":
            continue
        else:
            return False
            break
    else:
        return True


name = input("Enter a name : ")
if validateName(name):
    print(name,"is a valid name")
else:
    print(name,"is not a valid name")


