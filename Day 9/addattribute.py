import pandas as pd

df = pd.read_csv(r"D:/python learning/Day 9/data.csv")

df["passed"] = df.score >= 80
print(df)
