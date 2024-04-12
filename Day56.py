# Day 56 of 100 days of coding challenge
# Program to generate 4 digit OTP
import random as rd
def OTPGenerate():
    otp = []
    i = 0
    while i < 4:
        digit = rd.randint(0,9)
        if digit not in otp:
            otp.append(digit)
            i += 1

    print("Your OTP is : ",end="")
    for j in range(4):
        print(otp[j],end=" ")


OTPGenerate()

