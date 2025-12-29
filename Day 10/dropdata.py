import pandas as pd

df = pd.read_csv("D:/Python Learning/Day 10/drop.csv")
## deleted those enteries that is not usable or have lot of details missing
df = df.dropna()
print(df)