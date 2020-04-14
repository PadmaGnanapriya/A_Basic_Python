import random
import numpy

print(random.choice(range(1,10)))                                  # 5
print(random.choice(random.choice([range(1,10),range(3,12)])))     # 9

print(numpy.random.random((5,2,3)))      # Generates a 5 x 2 x 3 NumPy array with random uniform values. correct
                                         # [[[0.16241141 0.66188217 0.38377861]
                                         #  [0.44952851 0.69184908 0.91335815]]
                                         #
                                         # [[0.45842057 0.01043012 0.06746588]
                                         #  [0.45454201 0.80623867 0.75776211]]
                                         #
                                         # [[0.56158265 0.74528977 0.02417009]
                                         #  [0.88930252 0.87919157 0.45368969]]
                                         #
                                         # [[0.60807638 0.31164551 0.42308134]
                                         #  [0.6507687  0.52230934 0.03222897]]
                                         #
                                         # [[0.51313747 0.62043215 0.78645941]
                                         #  [0.60209728 0.03556762 0.00534252]]]


print(numpy.random.normal(1,2,3))   # Generates 3 samples with mean 1 and standard deviation 2
                                    # [-2.18263859  2.09581854 -1.0632472 ]


print(numpy.random.randint(1,5,(2,3)))      # Generates a 2 x 3 array with random integers from 1-4.
                                            # [[3 2 3]
                                            #  [2 3 3]]