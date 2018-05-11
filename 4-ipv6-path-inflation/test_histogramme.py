

import random
import numpy
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker



#x = [ random.randint(1, 50) for _ in range(100)]
y = [random.randint(1, 10) for _ in range(100)]
x= [1, 1, 1, 1, 2, 2, 10,10,15,15 ]
bins = numpy.linspace(0,20,5)

plt.hist(x, bins,rwidth=0.8)

plt.xlabel('numbers')
plt.ylabel('frequency')
#plt.xscale('log')
plt.grid(True)
formatter = mticker.PercentFormatter(xmax=10)
plt.gca().yaxis.set_major_formatter(formatter)

plt.show()
#plt.legend(loc='upper right')
plt.show()
#plt.savefig("E:\semestre 4\ecosysteme et evolution de l'Internet\plots\hist")
