#!/usr/bin/env python

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import random

n=100
#x0=np.linspace(-np.pi, np.pi, n)
x0=np.linspace(0, 5, n) # read in this many files
#y0=np.linspace(-np.pi, np.pi, n) 
y0=np.linspace(0, 0.1, n) # for each file, get the y values, assumed to be 0.001 spaced apart

x,y=np.meshgrid(x0,y0)
z=np.sin(x)*0.001*random.randint(0,1000)+np.cos(y)*0.001*random.randint(0,1000)
# z = [the values from the file for each line]

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_wireframe(x,y,z,rstride=5,cstride=5)
#plt.show()


for angle in range(0,90):
	ax.view_init(30,angle)
	plt.draw()
	plt.pause(.001)


# x make up some crane, span-wise values; put in header line of each file; e.g. x=40.0 and parse that
# y infer some chord-wise values based on the sampling index 
# z the values in the file at each index 
# 
# identify a set of files; read those files in one by one; these are the y and z 
# read the header line of the files; create the x vector