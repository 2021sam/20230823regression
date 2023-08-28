import matplotlib.pyplot as plt


data = [(1, 1), (2, 1), (3, 2), (4, 2), (5, 4)]
# data = [(43,41), (44,45), (45,49), (46,47), (47,44)]
# print(data)

X = [x[0] for x in data]
Y = [y[1] for y in data]
xbar = sum(X) / len(X)
ybar = sum(Y) / len(Y)



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
L = 0.00001
epochs = 100000
n = len(X)

for i in range(epochs):
    m, b = gradient_descent(m, b, X, Y, n, L)

print(m, b)