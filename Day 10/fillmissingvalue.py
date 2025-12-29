import pandas as pd
df = pd.read_csv("D:/Python Learning/Day 10/messydata.csv")

## convert any data in column to numeric or if not then error less
df["age"] = pd.to_numeric(df["age"],errors = "coerce")
df["experience"] = pd.to_numeric(df["experience"],errors = "coerce")
df["score"] = pd.to_numeric(df["score"],errors = "coerce")


df["age"].fillna(df["age"].mean(), inplace = True)
df["experience"].fillna(0, inplace = True)
df["score"].fillna(df["score"].mean(), inplace = True)

print(df)