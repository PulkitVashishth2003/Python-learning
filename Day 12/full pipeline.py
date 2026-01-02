import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

file_path = r"D:\Python learning\Day 11\MINI PROJECT — ML-READY FEATURE PIPELINE\final.csv"
##df = pd.read_csv("D:/Python learning/Day 11/MINI PROJECT — ML-READY FEATURE PIPELINE/final.csv")
try:
    df = pd.read_csv(file_path)
    df['experience level'] = df['experience level'].map({'Junior': 0, 'Senior': 1})
    x = df.drop("score", axis = 1)
    y = df["score"]

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state = 34)
    model = LinearRegression()
    model.fit(x_train,y_train)

    predictions = model.predict(x_test)
    mse = mean_squared_error(y_test, predictions)
    print("MSE:", mse)

except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}")
    print("Check if the folder name uses a standard hyphen '-' instead of a long dash '—'.")
except Exception as e:
    print(f"An error occurred: {e}")