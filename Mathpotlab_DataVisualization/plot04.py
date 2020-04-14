import matplotlib.pyplot as plt
x = range(10)
plt.plot(x,[x1 for x1 in x],x,[x1*2 for x1 in x], x,[x1*4 for x1 in x])
plt.grid(True)
plt.axis([-1,5,-1,10])
plt.show()