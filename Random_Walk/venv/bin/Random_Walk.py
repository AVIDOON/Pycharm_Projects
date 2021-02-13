import numpy as np
import matplotlib.pyplot as pl
import random as rand

p = np.zeros(5)


n = 1000

for i in range(1,n-1):
   val = rand.random(1,2)
if val == 1:
    p[i+1] = p[i] + 1
else:
    p[i+1] = p[i] - 1

    pl.plot(x)
    plt.show()



