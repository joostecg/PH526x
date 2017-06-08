import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=1000)
plt.hist(x)
plt.show()


x = np.random.normal(size=1000)
plt.hist(x, normed=True, bins=np.linspace(-5,5,21))
plt.show()

x = np.random.gamma(2,3,100000)

plt.figure()
plt.subplot(221)
plt.hist(x, bins = 30)
plt.subplot(222)
plt.hist(x, bins=30, normed=True)
plt.subplot(223)
plt.hist(x, bins=30, cumulative=30)
plt.subplot(224)
plt.hist(x, bins = 30, normed=True, cumulative=30, histtype="step")
plt.show()