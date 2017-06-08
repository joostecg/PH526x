import numpy as np
import matplotlib.pyplot as plt

np.random.random()


np.random.random(5)

np.random.random((5,3))


np.random.normal(0,1)

np.random.normal(0,1,5)

np.random.normal(0,1, (2,5))

np.random.randint(1,7)

X = np.random.randint(1,7, (10,3))

# X

# X.shape

# np.sum(X)

#np.sum(X, axis=0)

Y = np.sum(X, axis=1)

# program for code
X = np.random.randint(1,7, (1000000,10))
Y = np.sum(X, axis=1)
plt.hist(Y,bins=100);
plt.show()


np.random.random((5,2,3))

np.random.normal(1,2,3)

np.random.randint(1,5,(2,3))

Z = np.sum(np.random.randint(1,7,(100,10)), axis=0)
Z.shape