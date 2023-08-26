# https://medium.com/analytics-vidhya/stock-prediction-using-linear-regression-cd1d8351f536



import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# pip install -U scikit-learn

data = yf.download('SPY')
plt.figure(figsize=(10, 5))
data['Close'].plot()

data = data.reset_index()
x = np.array(data.index).reshape(-1, 1)
y = data['Close']

linreg = LinearRegression().fit(x, y)
linreg.score(x, y)
predictions = linreg.predict(x)

plt.figure(figsize=(15,5))
plt.plot(data['Close'])
plt.plot(data.index, predictions)
plt.show()

print('R^2:', linreg.score(x, y))
