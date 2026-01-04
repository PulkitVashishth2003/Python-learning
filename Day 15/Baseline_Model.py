import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("D:/Python Learning/Day 13/classification_data.csv")

x = df.drop("selected", axis=1)
y = df["selected"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(x_train, y_train)

predictions = model.predict(x_test)
print("Baseline Accuracy:", accuracy_score(y_test, predictions))
