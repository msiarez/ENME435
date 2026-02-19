import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)

y = np.sin(x)

plt.figure(1)
plt.plot(x,y,'bo-')

plt.figure(2)
plt.plot(x,y/2,'r--',label="y2")
plt.grid()

plt.title("Figure 2 Title Here")
plt.xlabel('X')
plt.ylabel('Y')

plt.legend()

plt.savefig('2192026.png')

plt.show()
