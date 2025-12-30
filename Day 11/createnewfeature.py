import pandas as pd
df = pd.read_csv("D:/Python Learning/Day 10/MINI PROJECT — AI-READY DATA CLEANING PIPELINE/clean_data.csv")
df["experience level"] = df["experience"].apply(
    lambda x : "Junior" if x < 2 else "Senior"
)
print (df)
df.to_csv("D:/Python Learning/Day 11/added_data.csv")