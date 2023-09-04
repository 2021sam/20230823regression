#   Plot a flat line
import matplotlib.pyplot as plt


X = [x for x in range(10)]
Y = [y for y in range(-5, 5)]
plt.plot(X, [1 for x in X])
plt.show()
