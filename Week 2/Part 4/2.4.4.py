import numpy as np
import random

import time

start_time = time.clock()

end_time = time.clock()

end_time - start_time

start_time = time.clock()
ys = []
for rep in range(1000000):        # start small with say 5 in range to test before going larger in the range
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)

end_time = time.clock()

print(end_time - start_time)


start_time = time.clock()
X = np.random.randint(1,7, (1000000,10))
Y = np.sum(X, axis=1)
end_time = time.clock()

print(end_time - start_time)

33.17593277630047/0.23425358651559236

