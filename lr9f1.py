#   Enter a Linear formula to create (x, y) data points.

import matplotlib.pyplot as plt

r = 5
#   Linear Formula
data = [(x, 3*x + 15) for x in range(-r, r+1)]
# data = [(0, 2), (1, 3), (2, 5), (3, 4)]
print('data:')
print(data)
X = [x[0] for x in data]
Y = [y[1] for y in data]
xbar = sum(X) / len(X)
ybar = sum(Y) / len(Y)
print(f'xbar = {xbar}')
print(f'ybar = {ybar}')
x_error = [x - xbar for x in X]
y_error = [y - ybar for y in Y]
sigma = 0
n = len(X)

# Least Squares 1
#       ∑ (xi - xbar)(yi - ybar)
# b =   ------------------------
#       ∑(xi - xbar)^2

numerator = [ (X[i] - xbar)*(Y[i] - ybar) for i in range(n) ]
denominator = [ (X[i] - xbar )**2 for i in range(n) ]
b = sum(numerator)/sum(denominator)
print('Least Squares 1:')
print(f'slope b = {b}')
a = ybar - b*xbar
print(f'a = {a}')
print(f'y = {b}x + {a}')


# Least Squares 2
# https://www.mathsisfun.com/data/least-squares-regression.html
# https://statisticsbyjim.com/regression/least-squares-regression-line/
# https://www.cuemath.com/data/least-squares/
# m = N ∑(xy) - ∑x∑y
#     --------------
#     N ∑(x^2) - (∑x)^2
# b = ∑y - m∑x
#     --------
#     N
print('\nLeast Squares 2:')
XY = [ X[i]*Y[i] for i in range(n)  ]
X_squared = [ X[i]*X[i] for i in range(n) ]
numerator = n * sum(XY) - (sum(X)*sum(Y))
denominator = n*sum(X_squared) - (sum(X)*sum(X))
m = numerator / denominator
b = (sum(Y) - m*sum(X)) / n
print(f'm = {m}')
print(f'b = {b}')
print(f'y = {m}x + {b}')


# Mean Squared Error - MSE
# https://www.geeksforgeeks.org/python-mean-squared-error/
# https://www.geeksforgeeks.org/python-mean-squared-error/
# for i in range(n):
#     y = m*X[i] + b
Yi = [m*X[i] + b for i in range(n)]
# y_error = [Y[i] - e for i in range(n)]
# print(Yi)

E = [Y[i] - Yi[i] for i in range(n)]
print(f'E = {E}')
E_squared = [E[i] * E[i] for i in range(n)]
print(f'E_squared = {E_squared}')
mse = sum(E_squared)/n
print(f'mse = {mse}')


plt.plot(X, Y)
plt.show()
