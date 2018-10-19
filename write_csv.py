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
    M=0.0004
    r1=M*(random.randint(0,1000)-500)
    r2=0.01*random.randint(0,100)
    y_noise[d]=y_noise[d]+r1
y_smooth = savgol_filter(y_noise,601,2)

total_len_x=0; total_len_y_raw=0; total_len_y_smooth=0; 
print len(x)
print len(y_noise)
print len(y_smooth)

for i in range(0,len(x)-1):
    total_len_x = total_len_x + sqrt(pow(float(x[i+1]) - float(x[i]),2))
    total_len_y_raw = total_len_y_raw + sqrt(pow(float(y_noise[i+1])-float(y_noise[i]),2) + pow(float(x[i+1]) - float(x[i]),2))
    total_len_y_smooth = total_len_y_smooth + sqrt(pow(float(y_smooth[i+1])-float(y_smooth[i]),2) + pow(float(x[i+1])-float(x[i]),2))

print "total_len_x is:  ", str(total_len_x)
print "total_len_y_raw is:  ", str(total_len_y_raw)
print "total_len_y_smooth is:  ", str(total_len_y_smooth)

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

