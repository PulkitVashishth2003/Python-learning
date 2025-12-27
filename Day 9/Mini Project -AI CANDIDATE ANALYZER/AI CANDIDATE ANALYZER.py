import pandas as pd

df = pd.read_csv(r"D:/python learning/Day 9/data.csv")

average_score = df.score.mean()

df["result"] = df.score.apply(
    lambda x: "Selected" if x >= average_score else "Rejected"
)

df.to_csv("D:/python learning/Day 9/Mini Project -AI CANDIDATE ANALYZER/final_candidates.csv", index=False)

print("Final dataset saved successfully")
print(df)
