import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11)
y1 = np.cos(x) - 1
y2 = 2 * np.sin(x / 3)
y3 = (x ** 2) / 20. - 2

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()
