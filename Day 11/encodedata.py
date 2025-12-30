import pandas as pd
df = pd.read_csv("D:/Python Learning/Day 10/MINI PROJECT — AI-READY DATA CLEANING PIPELINE/clean_data.csv")
new_df = pd.get_dummies(df, columns = ["name"])
print(new_df)