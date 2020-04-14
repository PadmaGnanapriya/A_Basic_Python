import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1,100)
plt.plot(y,'--',y*5,'-.',y*10, ':')
plt.show()

jj=np.arange(-10,50)
plt.plot(jj*4-40,'c')
plt.plot(jj**1.2,'g')
plt.plot(jj,'y')
plt.plot(jj**0.5,'r')
plt.plot(-jj,'m')
plt.show()