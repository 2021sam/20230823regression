#   Plot a non linear curve
import matplotlib.pyplot as plt

X = [x for x in range(-10, 10)]
Y = [2*x*x for x in X]
plt.plot(X, Y)
plt.show()
