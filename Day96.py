# Day 96 of 100 days of coding challenge
# Program to create a pie chart
import matplotlib.pyplot as plt
subjects = ["CS","IP","IT"]
students = [45,78,16]
plt.pie(students,colors=["red","blue","yellow"],labels=subjects)
plt.title("Students Opting for CS/IP/IT")
plt.show()

