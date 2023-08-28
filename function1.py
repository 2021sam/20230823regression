import matplotlib.pyplot as plt


X = [x for x in range(10)]
# print(X)
Y = [y for y in range(-5, 5)]
# print(Y)
# plt.figure(figsize=(15,5))
one = lambda x: 1
# Z = [one(x) for x in range(10)]
# Z = [1 for x in range(10)]

# print(Z)
# plt.plot(X, X)
# plt.plot(X, Y)
plt.plot(X, [1 for x in X])
# plt.plot(X, [1 for x in range(10)] )
# plt.plot(Y)
plt.show()
