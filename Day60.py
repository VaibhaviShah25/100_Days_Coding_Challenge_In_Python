# Day 60 of 100 days of coding challenge
# Program to create a login screen
d = {'shraddha':'cpp','jk':'python','avinash':'javascript'}
def signup(user,passw):
    if user not in d:
        d[user.lower()] = passw.lower()
        print("Data added successfully")
    else:
        print("Username already exists")
def Login(userid,passw):

    for i in range(3):
        if userid.lower() in d and d[userid] == passw.lower():
            print("Password Matched!")
            print("Access Granted")
            break
        else:
            print("Invalid userid or password ")
    else:
        print("Access Denied ")

print("<>"*15)
print("\t\tLOGIN SCREEN")
print("<>"*15)
print("Press 1 - Login\nPress 2 - SingUP")
choice = int(input("Enter your choice : "))
if choice == 1:
    user = input("Enter username : ")
    password = input("Enter password : ")
    Login(user,password)
elif choice == 2:
    user = input("Enter username : ")
    password = input("Enter password : ")
    signup(user,password)
    print(d)
print("<>"*15)

