# Day 99 of 100 days of coding challenge
# Program to do data analysis using Pandas

import pandas as pd

stu = {'Rohit':90,'Kanak':78,'Rahul':96,'Priya':67,'Riya':94}
S = pd.Series(stu)
print(S)
print(S.nbytes)          # nbytes attribute
print(S[S >= 80])        # shows only rows which have marks >= 80
print(S + 2)             # adds 2 to every value in Series
print('Maximum Marks :',S.max(),'\nMinimum Marks :',S.min())   # max, min method










