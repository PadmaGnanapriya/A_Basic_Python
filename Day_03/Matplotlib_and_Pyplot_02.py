import matplotlib.pyplot as plt

import numpy as np
x = np.linspace(1,10,20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x,y1,"bo-",linewidth=2,markersize=4)
plt.show()