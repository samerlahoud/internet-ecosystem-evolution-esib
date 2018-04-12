import random
import numpy
import matplotlib.pyplot as plt




x = [ random.randint(1, 50) for _ in range(400)]
y = [random.randint(1, 10) for _ in range(100)]

bins = numpy.linspace(0,50,100)
plt.hist([x,y], bins,color=['green','blue'],label=['x','y'])

plt.xlabel('numbers')
plt.ylabel('frequency')
plt.grid(True)
plt.legend(loc='upper right')
plt.show()
#plt.savefig("E:\semestre 4\ecosysteme et evolution de l'Internet\plots\hist")
