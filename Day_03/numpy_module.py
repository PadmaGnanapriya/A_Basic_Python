import numpy as np
zero_vector=np.zeros(5)
zero_matrix=np.zeros((5,3))

print(zero_vector)       #[0. 0. 0. 0. 0.]

print(zero_matrix)       # [[0. 0. 0.]
                         # [0. 0. 0.]
                         # [0. 0. 0.]
                         # [0. 0. 0.]
                         # [0. 0. 0.]]



x = np.array([[3,6],[5,7]])
y = x.transpose()
print(y)       # [[3 5][6 7]]

a=[2,4]
b=[6,3]
c=[1,2,3]
print(c[:2])                    # [1, 2]
print(a+b)                      # [2, 4, 6, 3]
print(np.array(a)+np.array(b))  # [8 7]

z1=np.array([1,3,5,7,9])
z2=z1+1
print(z2)                        # [ 2  4  6  8 10]
ind=[0,2,3]
print(z2[ind])                   # [2 6 8]
print( z2 > 6 )                  # [False False False  True  True]


a = np.array([1,2])
b = np.array([3,4,5])
print(b[a])                     # [4 5]

kk=np.linspace(0,100,10)
print(kk)                       # [  0.          11.11111111  22.22222222  33.33333333  44.44444444  55.55555556  66.66666667  77.77777778  88.88888889 100.        ]