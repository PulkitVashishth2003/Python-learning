import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("D:/Python learning/Day 11/added_data.csv")
df = pd.get_dummies(df, columns = ["name"])

scaler = StandardScaler()

num_col = ["age","experience","score"]
df[num_col] = scaler.fit_transform(df[num_col])

df.to_csv("D:\Python learning\Day 11\MINI PROJECT — ML-READY FEATURE PIPELINE/final.csv")

print("new file created successfully........")