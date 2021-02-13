import numpy as np
import matplotlib.pyplot as plt
import random as rd

n = 5

x = np.zeros(n)
y = np.zeros(n)

for i,j in range(1, n):
    val = rd.randint(1, 2)
    if val == 1 and i==1:
         x[i] = x[i - 1] - 1
         x[j] = x[j - 1] - 1

             x[i]=x[i-1]
             x[j]=x[j-1]
    else:
        x[i] = x[i - 1] + 1
        x[j] = x[j - 1] + 1



plt.title("Random 2D-Walk for " + str(n) + " steps")
plt.plot(x, y)
plt.show()
