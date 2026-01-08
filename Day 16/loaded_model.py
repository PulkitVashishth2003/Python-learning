import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("D:/Python Learning/Day 13/classification_data.csv")

X = df.drop("selected", axis=1)
y = df["selected"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

joblib.dump(model, "D:/Python Learning/Day 16/final_model.pkl")

loaded_model = joblib.load("D:/Python Learning/Day 16/final_model.pkl")
preds = loaded_model.predict(X_test)

print("Predictions after reload:", preds)
print ("The program ends here")
