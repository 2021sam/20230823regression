import matplotlib.pyplot as plt

X = [x for x in range(-10, 10)]
# Y = [1 for x in X]
Y = [2*x*x for x in X]

print(X)
print(Y)

plt.plot(X, Y)
plt.show()
