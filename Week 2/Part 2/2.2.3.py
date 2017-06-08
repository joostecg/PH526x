import numpy as np

z1 = np.array([1,3,5,7,9])
z2 = z1 + 1

z1
z2

ind = [0,2,3]
z1[ind]

ind = np.array([0,2,3])
z1[ind]

z1 > 6

z1[z1 > 6]
z2[z1 > 6]

ind = z1 > 6
ind

z1[ind]
z2[ind]

w = z1[0:3]
w
w[0] = 3
w
z1

ind = np.array([0,1,2])
w = z1[ind]

w[0] = 3
w
z1

a = np.array([1,2])
b = np.array([3,4,5])
b[a]
c = b[1:]
b[a] is c
c