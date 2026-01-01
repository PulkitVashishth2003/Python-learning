import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


df = pd.read_csv("D:/Python learning/Day 11/MINI PROJECT — ML-READY FEATURE PIPELINE/final.csv")

x = df.drop("score", axis = 1)
y = df["score"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state = 34)
model = LinearRegression()
model.fit(x_train,y_train)

predictions = model.predict(x_test)
mse = mean_squared_error(y_test, predictions)
print("MSE:", mse)