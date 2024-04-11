# Day 51 of 100 days of coding challenge in Python
# Program to create a dictionary for employee using functions
def create(demp, nemp):
    for i in range(nemp):
        empid = int(input("Enter employee id : "))
        name = input("Enter name of the employee : ")
        job = input("Enter job : ")
        sal = eval(input("Enter salary of the employee : "))
        demp[empid] = [name, job, sal]


n = int(input("Enter the number of employees : "))
d = {}
create(d, n)
print("Dictionary of employee data is\n", d)

