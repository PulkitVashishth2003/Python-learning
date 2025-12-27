#importing pandas library and named it pd
import pandas as pd
##created datafram "data" which takes data from given file and arrange in given column names
data = pd.read_csv(r"D:\Python learning\Day 9\data.csv")
## to print the data in tabular form
##df = pd.Series(r"D:\Python learning\Day 9\data.csv")
##print(data)
print(data)
## to print the type of data
print(type(data))