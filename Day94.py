# Day 94 of 100 days of coding challenge
# Program to create a bar chart
import matplotlib.pyplot as plt
sub = ['Maths-2','BEE','EM','Chemistry','EG']
marks = [95,90,85,92,75]
plt.bar(sub,marks,color=('Blue','red','orange','green','yellow'))
plt.title("Student Report")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

