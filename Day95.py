# Day 95 of 100 days of coding challenge
# Program to create a line chart
# Below program shows score of MS Dhoni in his IPL career till date
import matplotlib.pyplot as plt

years = ["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"]
scores = [413,332,287,392,358,461,371,372,284,290,455,416,200,114,232,104,136]
plt.plot(years,scores,color="#FFD700")
plt.title("Score of MS Dhoni in IPL")
plt.xlabel("Years")
plt.ylabel("Scores")
plt.show()

