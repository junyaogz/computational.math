# Perfect Heart Shape

import numpy as np
from matplotlib import pyplot as plt

theta = np.linspace(0, 2 * np.pi, 10)

x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

plt.plot(x, y,"bo-")
plt.title('Heart Shape - 10 points')
plt.show()

theta = np.linspace(0, 2 * np.pi, 20)

x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

plt.plot(x, y,"bo-")
plt.title('Heart Shape - 20 points')
plt.show()

theta = np.linspace(0, 2 * np.pi, 50)

x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

plt.plot(x, y,"bo-")
plt.title('Heart Shape - 50 points')
plt.show()

theta = np.linspace(0, 2 * np.pi, 100)

x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

plt.plot(x, y,"b-")
plt.title('Heart Shape - 100 points')
plt.show()
