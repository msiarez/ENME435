import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)

y = np.sin(x)

plt.plot(x,y,'b')
plt.plot(x,y/2,'r')
plt.show()
