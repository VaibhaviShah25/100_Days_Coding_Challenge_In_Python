# Day 52 of 100 days of coding challenge
# Program to search and update an employee in dictionary
def create(demp, nemp):
    for i in range(nemp):
        empid = int(input("Enter employee id : "))
        name = input("Enter name of the employee : ")
        job = input("Enter job : ")
        sal = eval(input("Enter salary of the employee : "))
        demp[empid] = [name, job, sal]

def updateemp(demp,empid):
    if empid in demp:
        demp[empid][2] += 25/100 * demp[empid][2] #increasing salary by 25%
        print("\nEmployee salary updated successfully! ")
    else:
        print("Employee not found ")

n = int(input("Enter the number of employees : "))
d = {}
create(d, n)
print("Dictionary of employee data is\n", d)
empid = int(input("Enter EmployeeID whose salary needs to be increased :"))
updateemp(d,empid)

