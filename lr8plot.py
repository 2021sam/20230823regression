# lr7.py
#   added matplotlib

import matplotlib.pyplot as plt

data = [(0, 2), (1, 3), (2, 5), (3, 4)]
X = [x[0] for x in data]
Y = [y[1] for y in data]
xbar = sum(X) / len(X)
ybar = sum(Y) / len(Y)
print(f'xbar = {xbar}')
print(f'ybar = {ybar}')

x_error = [x - xbar for x in X]
y_error = [y - ybar for y in Y]
# print(y_error)

sigma = 0
n = len(X)

# Least Squares 1
# # sigma 1-n (xi - xbar)(yi - ybar)
# sig = [x_error[i] * y_error[i] for i in range(n) ]
# print(sig)
# numerator = sum(sig)
# print(numerator)
# x_error_squared = [e*e for e in x_error]
# beta = numerator / sum(x_error_squared)
# print(beta)
# # y_error_squared = [e*e for e in y_error]
# # print(y_error_squared)
# # print(sum(y_error_squared))
# # variance = sum(y_error_squared) / len(Y)
# # print(variance)

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

XY = [ X[i]*Y[i] for i in range(n)  ]
X_squared = [ X[i]*X[i] for i in range(n) ]
numerator = n * sum(XY) - (sum(X)*sum(Y))
denominator = n*sum(X_squared) - (sum(X)*sum(X))
m = numerator / denominator
b = (sum(Y) - m*sum(X)) / n
print(f'm = {m}')
print(f'b = {b}')



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
