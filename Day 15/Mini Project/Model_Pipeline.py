import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("D:/Python Learning/Day 13/classification_data.csv")

X = df.drop("selected", axis=1)
y = df["selected"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

configs = [1.0, 0.1, 0.01]

best_score = 0
best_model = None

for c in configs:
    model = LogisticRegression(C=c, max_iter=1000)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    score = accuracy_score(y_test, preds)

    print(f"C={c} → Accuracy={score}")

    if score > best_score:
        best_score = score
        best_model = model

print("Best model accuracy:", best_score)
