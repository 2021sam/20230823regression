import pandas as pd
import numpy as np

dataset = pd.read_csv('prowork.csv')
print(dataset.shape)
print(dataset.head())

x = dataset['Years of School'].values
y = dataset['Salary'].values
# print( type ( x ))
# print(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
print(x_mean, y_mean)
