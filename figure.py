import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-10,9,20)
y= x**3
z=x**2

#1. ÖRNEK

# figure= plt.figure()

# axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
# axes_cube.plot(x,y,'o--r')
# axes_cube.set_xlabel("X Axis")
# axes_cube.set_ylabel("Y Axis")
# axes_cube.set_title("Cube")

# axes_square=figure.add_axes([0.17,0.6,0.25,0.25])

# axes_square.plot(x,y,'b')
# axes_square.set_xlabel("X Axis")
# axes_square.set_ylabel("Y Axis")
# axes_square.set_title("Square")

# #2. ÖRNEK

# figure=plt.figure()
# axes=figure.add_axes([0,0,1,1])

# axes.plot(x,y, label="cube")
# axes.plot(x,z, label="square")

# plt.legend(loc=4)

#3. ÖRNEK

fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(4,4))

axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure2.pdf")

plt.show()

