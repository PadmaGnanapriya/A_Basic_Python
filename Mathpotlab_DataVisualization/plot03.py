import matplotlib.pyplot as plt
import numpy

x = range(11)

plt.plot(x, [i**2for i in x])
plt.plot(x, [i**10 for i in x])
plt.plot(x, [i**i for i in x])

plt.show()