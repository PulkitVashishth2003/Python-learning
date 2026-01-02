import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

file_path = r"D:\Python learning\Day 11\MINI PROJECT — ML-READY FEATURE PIPELINE\final.csv"
df = pd.read_csv(file_path)
df['experience level'] = df['experience level'].map({'Junior': 0, 'Senior': 1})
X = df.drop("score", axis=1)
y = df["score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)

print("Predicted Scores:", predictions)
print("Actual Scores:", y_test.values)
print("Model Error:", mse)
