import matplotlib.pyplot as plt
import numpy as np 

my_x = np.linspace(-1,1)
my_y = np.sin(my_x)

plt.plot(my_x,my_y)
title="Plot"
filename= "Plot.jpg"

plt.title(title)
plt.savefig(filename)
