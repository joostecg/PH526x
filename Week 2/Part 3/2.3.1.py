import matplotlib.pyplot as plt

plt.plot([0,1,4,9,16]);

import numpy as np
x = np.linspace(0 , 10, 20)
y = x**2.0
x
y
plt.plot(x,y)
plt.show()

x = np.linspace(0 , 10, 20)
y1 = x**2.0
y2 = x**1.5

plt.plot(x,y1,"bo-")

plt.plot(x,y1,"bo-", linewidth=2, markersize=4)

plt.plot(x,y2,"gs-", linewidth=2, markersize=12)

plt.show()

plt.plot([0,1,2],[0,1,4],"rd-")
plt.show()
