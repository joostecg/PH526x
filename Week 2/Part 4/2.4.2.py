import random
import numpy as np
import matplotlib.pyplot as plt

random.choice([1,2,3,4,5,6])

rolls = []
for k in range(100):
    rolls.append(random.choice([1,2,3,4,5,6]))

#len(rolls)

#rolls

plt.hist(rolls, bins=np.linspace(0.5, 6.5, 7))
plt.show()

# rule of large numbers is that expect average to have all number almost the same
rolls = []
for k in range(1000000):
    rolls.append(random.choice([1,2,3,4,5,6]))

plt.hist(rolls, bins=np.linspace(0.5, 6.5, 7));
plt.show()



# rolling of 10 dice and summating them

ys = []
for rep in range(1000000):        # start small with say 5 in range to test before going larger in the range
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)

# len(ys)
# ys
#
# min(ys)
# max(ys)

plt.hist(ys);
plt.show()
