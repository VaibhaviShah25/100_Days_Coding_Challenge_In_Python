# Day 55 of 100 days of coding challenge
# Program to check if an emailId is valid or not
def emailValidate(email):
    i = 0
    if email.endswith(".com"):
        if email[0] != "@" and email.count("@") == 1:
            while email[i] != "@":
                if email[i].isalpha() or email[i].isdigit():
                    i += 1
                    continue
                elif email[i] == "_" and email.count("_") == 1:
                    i += 1
                    continue
                else:
                    print("Not a valid emailId")
                    break

            else:
                print("Valid emailId")
        else:
            print("Not a valid emailId")
    else:
        print("Not a valid emailId")


email = input(" Enter your emailId : ")
emailValidate(email)
