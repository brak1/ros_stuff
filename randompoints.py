#!/usr/bin/env python

from mpl_toolkits.mplot3d import axes3d
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import numpy as np
import random
from math import sqrt

n=1000
D=40.0
p=np.linspace(0,100,n)
z=D+(n/2)*pow((p/n),2)
s=D+(n/2)*pow((p/n),2)

for d in range(0,n):
	r=0.002*(random.randint(0,1000)-500)
	s[d]=s[d]+r

s_smooth = savgol_filter(s, 401, 2) # window size 51, polynomial order 3import matplotlib.pyplot as plt
s_smooth2 = savgol_filter(s,51,4)
s_smooth3 = savgol_filter(s,101,2)

fig=plt.figure()
fig.suptitle("Plotted Curve with Noise and Smoothing Samples")
fig.subplots_adjust(left=0.1, wspace=0.4, hspace = 0.4)

sub1=fig.add_subplot(221)
sub1.plot(p,s)
sub1.plot(p,z)
sub1.set_title("'s' with noise and original 'z'")

sub2=fig.add_subplot(222)
sub2.plot(p,s_smooth)
sub2.plot(p,z)
sub2.set_title("s_smooth")

sub3=fig.add_subplot(223)
sub3.plot(p,s_smooth2)
sub3.plot(p,z)
sub3.set_title("s_smooth2")

sub4=fig.add_subplot(224)
sub4.plot(p,s_smooth3)
sub4.plot(p,z)
sub4.set_title("s_smooth3")

total_len=0; total_len2=0; total_len3=0; total_len4=0; total_lenp=0; total_lenz=0;  
for i in range(0,n-1):
	total_len = total_len + sqrt(pow(s[i+1]-s[i],2) + pow(p[i+1]-p[i],2))
	total_len2 = total_len2 + sqrt(pow(s_smooth[i+1]-s_smooth[i],2) + pow(p[i+1]-p[i],2))
	total_len3 = total_len3 + sqrt(pow(s_smooth2[i+1]-s_smooth2[i],2) + pow(p[i+1]-p[i],2))
	total_len4 = total_len4 + sqrt(pow(s_smooth3[i+1]-s_smooth3[i],2) + pow(p[i+1]-p[i],2))
	total_lenp = total_lenp + (p[i+1]-p[i])
	total_lenz = total_lenz + sqrt(pow(z[i+1]-z[i],2) + pow(p[i+1]-p[i],2))
	
print "length of 's' = ", total_len
print "length of 's_smooth' = ", total_len2
print "length of 's_smooth2' = ", total_len3
print "length of 's_smooth3' = ", total_len4
print "length of 'p' = ", total_lenp
print "length of 'z' = ", total_lenz

plt.show()
