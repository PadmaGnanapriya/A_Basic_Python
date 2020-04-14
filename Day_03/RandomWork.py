import matplotlib.pyplot as plt
import numpy as np

number_of_steps=20
X_0= np.array([[0],[0]])
delta_X=np.random.normal(0,1,(2,number_of_steps))
X=np.concatenate((X_0,np.cumsum(delta_X,axis=1)),axis=1)
plt.plot(X[0],X[1],"ro-")
plt.show()
plt.savefig("RandomWork.png")