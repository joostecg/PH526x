import numpy as np

x = np.array([1,2,3])
y = np.array([2,4,6])
X = np.array([[1,2,3],[4,5,6]])
Y = np.array([[2,4,6],[8,10,12]])

x[2]
x[0:2]

z = x + y
z

X[:,1]
Y[:,1]
X[:,1] + Y[:,1]
X[1,:] + Y[1,:]
X[1]

[2,4] + [6,8]

np.array([2,4]) + np.array([6,8])


x = np.array([1,2,5])
x[1:2]