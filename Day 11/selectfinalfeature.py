import pandas as pd 
df = pd.read_csv("D:/Python Learning/Day 10/MINI PROJECT — AI-READY DATA CLEANING PIPELINE/clean_data.csv")
## shows the selected data that we mentioned in the code
feature = df[["age","experience","name"]]
print (feature)