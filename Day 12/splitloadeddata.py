import pandas as pd 
from sklearn.model_selection import train_test_split 

df = pd.read_csv("D:\Python learning\Day 11\MINI PROJECT — ML-READY FEATURE PIPELINE/final.csv")
x = df.drop("score", axis = 1)
y = df["score"]

x_train, y_train, x_test, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Training samples:", len(x_train))
print("Testing samples:", len(y_test))