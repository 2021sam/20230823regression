# data = [(1, 1), (2, 1), (3, 2), (4, 2), (5, 4)]
data = [(43,41), (44,45), (45,49), (46,47), (47,44)]
# print(data)
# print(data[2][1])
X = [x[0] for x in data]
Y = [y[1] for y in data]
xbar = sum(X) / len(X)
ybar = sum(Y) / len(Y)
print(ybar)

y_error = [e - ybar for e in Y]
print(y_error)
y_error_squared = [e*e for e in y_error]
print(y_error_squared)
print(sum(y_error_squared))
variance = sum(y_error_squared) / len(Y)
print(variance)





