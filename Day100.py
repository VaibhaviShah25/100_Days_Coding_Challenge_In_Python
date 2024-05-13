# Day 100 of 100 days of coding challenge
# Program to do data analysis using pandas library

import pandas as pd
c1 = [1900,2100,1400,1800]
c2 = [1600,2200,1500,1600]
c3 = [2600,2200,1800,1600]
years = ['2018','2019','2020','2021']
df = pd.DataFrame({'Years':years,'Comapany A':c1,'Company B':c2,'Company C':c3})
print(df)
print(df.values)   # print values of dataframe
print(df.size)     # print size of dataframe



