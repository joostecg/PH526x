import numpy as np

np.linspace(0, 100, 10)

np.logspace(1, 2, 10) # careful to use log values

np.logspace(np.log10(250), np.log10(500), 10)

X = np.array([[1,2,3],[4,5,6]])

X.shape

X.size

x = np.random.random(10)

np.any(x > 0.9)

np.all(x >= 0.1)

x


x=19
not np.any([x%i == 0 for i in range(2, x)])     # test for prime