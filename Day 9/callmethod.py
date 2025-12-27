import pandas as pd

df = pd.read_csv(r"D:/python learning/Day 9/data.csv")

print("Average score:", df.score.mean())
print("Max score:", df.score.max())
