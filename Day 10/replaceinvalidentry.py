import pandas as pd

df = pd.read_csv("D:/Python Learning/Day 10/messydata.csv")
df.replace("?",None,inplace = True)
print(df)