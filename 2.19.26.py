import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)

y = np.sin(x)

plt.figure(1)
plt.plot(x,y,'b')

plt.figure(2)
plt.plot(x,y/2,'r')
plt.grid()

plt.show()
