import numpy as np
import matplotlib.pyplot as plt


delta_X = np.random.normal(0,1,(2,5))
plt.plot(delta_X[0],delta_X[1], "go");
plt.show()


for k in range(5):
    delta_X = np.random.normal(0,1,(2,5))



X = np.cumsum(delta_X, axis=1)
X
delta_X


x = []
X_0 = np.array([[0],[0]])
delta_X = np.random.normal(0,1,(2,10000))
# X = np.cumsum(delta_X, axis=1)
X = np.concatenate((X_0, np.cumsum(delta_X, axis=1)), axis=1)
plt.plot(X[0],X[1], "ro-");
plt.savefig("randomwalk_5.png")
plt.show()