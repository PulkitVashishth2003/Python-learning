import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("D:/Python Learning/Day 13/classification_data.csv")

X = df.drop("selected", axis=1)
y = df["selected"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Train size:", len(X_train))
print("Test size:", len(X_test))
