import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('prowork.csv')
print(dataset.shape)
# print(dataset.head())

X = dataset['Years of School'].values
Y = dataset.iloc[:,1].values
# print( X.shape )

def gradient_descent(m_now, b_now, xdata, ydata, n, L):
    m_gradient = b_gradient = 0
    for i in range(n):
        x = xdata[i]
        y = ydata[i]
        # print(x, y)
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b



m = b = 0
L = 0.0001
epochs = 1000
n = len(X)

for i in range(epochs):
    m, b = gradient_descent(m, b, X, Y, n, L)

# print(m, b)
plt.scatter(X, Y, color='blue')
plt.plot(list(range(0, 15)), [m*x+b for x in range(0, 15)], color ="red")
plt.show()
