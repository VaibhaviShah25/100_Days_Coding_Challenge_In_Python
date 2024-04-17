# Day 64 of 100 days of coding challenge
# Program to create a contact book using Binary files
import pickle
import os
def add():
    name = input("Enter name : ")
    ph = input("Enter phone number : ")
    f = open("contacts.dat","ab")
    data = [name,ph]
    pickle.dump(data,f)
    f.close()
    print("Contact Added successfully!")

def display():
    f = open("contacts.dat","rb")
    print("Name\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            print(data[0]+"\t\t"+data[1])
    except:
        f.close()

def search():
    name = input("Enter name : ")
    f = open("contacts.dat","rb")
    print("Name\t\tContact")
    n = 0
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                print(data[0]+"\t\t"+data[1])
                n += 1
    except:
        f.close()
    if n == 0:
        print("No such contact found!")

def update():
    name = input("Enter contact name to be updated : ")
    f = open("contacts.dat","rb")
    g = open("temp.dat","ab")
    n = 0
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                ph = input("Enter updated phone number : ")
                data[1] = ph
                n += 1
            pickle.dump(data,g)
    except:
        f.close()
        g.close()
    os.remove("contacts.dat")
    os.rename("temp.dat","contacts.dat")
    if n == 0:
        print("No such contact found!")
    else:
        print("Contact updated successfully!")

def delete():
    name = input("Enter contact name to be deleted : ")
    f = open("contacts.dat", "rb")
    g = open("temp.dat", "ab")
    n = 0
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                print("Deleted contact is",data[0]+"\t\t"+data[1])
                n += 1
            else:
                pickle.dump(data, g)
    except:
        f.close()
        g.close()
    os.remove("contacts.dat")
    os.rename("temp.dat", "contacts.dat")
    if n == 0:
        print("No such contact found!")
    else:
        print("Contact deleted successfully!")

while True:
    print("<>"*20)
    print("Press 1 - Add a phone number ")
    print("Press 2 - Display all numbers ")
    print("Press 3 - Search a number ")
    print("Press 4 - Update a contact ")
    print("Press 5 - Delete a contact ")
    print("Press any other number to EXIT")
    print("<>"*20)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        add()
    elif choice == 2:
        display()
    elif choice == 3:
        search()
    elif choice == 4:
        update()
    elif choice == 5:
        delete()
    else:
        break
