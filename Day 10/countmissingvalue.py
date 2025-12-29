import pandas as pd

df = pd.read_csv("D:/Python Learning/Day 10/messydata.csv")

##print(df)
##print(df.isnull())
print(df.isnull().sum())