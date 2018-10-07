#!/usr/bin/env python

import csv
import random
import numpy as np
import matplotlib.pyplot as plt
from _ast import Num
from math import sqrt
from mpl_toolkits.mplot3d import axes3d
from scipy.signal import savgol_filter

n=1000
x=np.linspace(0,100,n)
y=(n/2)*pow(((x-50)/n),2)
y_noise=(n/2)*pow(((x-50)/n),2)
for d in range(0,n):
    M=0.0002
    r1=M*(random.randint(0,1000)-500)
    r2=0.01*random.randint(0,100)
    y_noise[d]=y_noise[d]+r1
y_smooth = savgol_filter(y_noise,101,2)

fig=plt.figure()
fig.suptitle("Plotting some crap I'm trying out")
fig.subplots_adjust(left=0.1, wspace=0.4, hspace = 0.4)

sub1=fig.add_subplot(311)
sub1.plot(x,y)
sub1.set_title("'y' needs some noises")

sub2=fig.add_subplot(312)
sub2.plot(x,y_noise)
sub2.set_title("y with noises")

sub3=fig.add_subplot(313)
sub3.plot(x,y_smooth)
sub3.plot(x,y)
sub3.set_title("y with savgol smooth")

plt.show()


#ifile  = open('sample.csv', "rb")

