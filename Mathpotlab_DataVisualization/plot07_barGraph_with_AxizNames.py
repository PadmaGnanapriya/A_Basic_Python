import matplotlib.pyplot as plt
import numpy

dictionary={'Chamara,':33,'Padma':83,'Pasindu':92,'Sunanda':82}
for i, key in enumerate(dictionary):plt.bar(i,dictionary[key])
plt.xticks(numpy.arange(len(dictionary)),dictionary.keys())
plt.show()