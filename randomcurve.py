#!/usr/bin/env python

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import random

n=100
x0=np.linspace(-np.pi, np.pi, n)
y0=np.linspace(-np.pi, np.pi, n) 

x,y=np.meshgrid(x0,y0)
z=np.sin(x)*0.001*random.randint(0,1000)+np.cos(y)*0.001*random.randint(0,1000)

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_wireframe(x,y,z,rstride=5,cstride=5)
#plt.show()


for angle in range(0,360):
	ax.view_init(30,angle)
	plt.draw()
	plt.pause(.001)

