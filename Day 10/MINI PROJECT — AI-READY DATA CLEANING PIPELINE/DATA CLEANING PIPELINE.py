import pandas as pd 
## load messy data in code
df = pd.read_csv("D:/Python Learning/Day 10/drop.csv")
## clean messy data
##df = df.isnull() ## checking all the null data
df.replace("?", None, inplace=True) ## put true to every "?" value
## filling all the missing data
df["age"] = pd.to_numeric( df["age"], errors = "coerce")
df["experience"] = pd.to_numeric(df["experience"], errors = "coerce")
df["score"] = pd.to_numeric(df["score"], errors = "coerce")

df["age"].fillna(df["age"].mean(), inplace = True)
df["experience"].fillna(df["experience"].mean(), inplace = True)
df["score"].fillna(df["score"].mean(), inplace = True)
df.to_csv("D:/Python Learning/Day 10/MINI PROJECT — AI-READY DATA CLEANING PIPELINE/clean_data.csv", index = False)
print("Cleaned Data Saved Successfully -->>")
print(df)
