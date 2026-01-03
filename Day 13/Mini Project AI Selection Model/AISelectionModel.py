import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


df = pd.read_csv("D:/Python Learning/Day 13/classification_data.csv")

X = df.drop("selected", axis=1)
y = df["selected"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)

print("Predictions:", predictions)
print("Actual:", y_test.values)
print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(cm)