import matplotlib.pyplot as plt


data = [(1, 1), (2, 1), (3, 2), (4, 2), (5, 4)]
# data = [(43,41), (44,45), (45,49), (46,47), (47,44)]
# print(data)

X = [x[0] for x in data]
Y = [y[1] for y in data]
xbar = sum(X) / len(X)
ybar = sum(Y) / len(Y)
print(f'xbar = {xbar}')
print(f'ybar = {ybar}')

x_error = [x - xbar for x in X]
y_error = [y - ybar for y in Y]
print(y_error)

sigma = 0
# for i in range(X):
#     sigma += x_error
n = len(X)
sig = [x_error[i] * y_error[i] for i in range(n) ]
print(sig)
numerator = sum(sig)
print(numerator)

x_error_squared = [e*e for e in x_error]

# y_error_squared = [e*e for e in y_error]
# print(y_error_squared)
# print(sum(y_error_squared))
# variance = sum(y_error_squared) / len(Y)
# print(variance)

beta = numerator / sum(x_error_squared)
print(beta)