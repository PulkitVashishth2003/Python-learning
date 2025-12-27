import pandas as pd

df = pd.read_csv(r"D:/python learning/Day 9/data.csv")

experienced = df[df.experience > 0]
print(experienced)
