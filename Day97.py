# Day 97 of 100 days of coding challenge
# Program to create a histogram
import matplotlib.pyplot as plt
Production = [144,160,123,134,135,119,189,143,195,167,175,177,116,190,189,153,172]
plt.hist(Production,bins=5)
plt.title('Frequency distribution of height')
plt.ylabel("Frequency")
plt.xlabel("Height")
plt.show()
