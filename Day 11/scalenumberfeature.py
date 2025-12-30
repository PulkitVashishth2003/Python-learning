import pandas as pd
from sklearn.preprocessing import StandardScaler    ## the StandardScaler contains the matematical equations
df = pd.read_csv("D:/Python Learning/Day 10/MINI PROJECT — AI-READY DATA CLEANING PIPELINE/clean_data.csv")

scaler = StandardScaler()
## this code transfer the mentioned columns in a eqaul condition (mean = 0 and standard deviation = 1)
## by this method we reduce the load on model if data has a to big ranges in each other
df[["age","experience","score"]] = scaler.fit_transform(df[["age","experience","score"]])

print (df)