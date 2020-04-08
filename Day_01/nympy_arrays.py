import numpy as np;
from pip._vendor.distro import name

x=np.array([2,5,7,9])
y=np.array([1,2,3,4,5,6,7])
print(x.mean())  #5.75
print(x.shape)   #(4,)
print(y.mean())  #4.5
print(y.shape)   #(7,)

print(np.sqrt(8))   #2.8284271247461903
import math as math;
print(math.sqrt(8))  #2.8284271247461903

#nympy sqrt can find square root of number set, but math sqrt can't
print(np.sqrt([8,9,16,25,45,24]))  #[2.82842712  3. 4. 5.  6.70820393  4.89897949]
# print(math.sqrt([8,9,16,25,45,24]))  Not execute


