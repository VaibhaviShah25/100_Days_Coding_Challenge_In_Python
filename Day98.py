# Day 98 of 100 days of coding challenge
# Program to create multiple bar graphs
import matplotlib.pyplot as plt
import pandas as pd

c1 = [1900,2100,1400,1800]
c2 = [1600,2200,1500,1600]
years = ['2018','2019','2020','2021']
df = pd.DataFrame({'Years':years,'Company A':c1,'Company B':c2})
df.index = df["Years"]
df.plot(kind="bar",color=['blue','#000040','blue','orange','pink'])
plt.title("Sales Records over 2018-2021")
plt.xlabel("Sale Year")
plt.ylabel("Sales in Lakhs INR")
plt.show()
