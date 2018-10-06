#!/usr/bin/env python

import csv
import random
import numpy as np
import matplotlib.pyplot as plt
from _ast import Num
from math import sqrt
from mpl_toolkits.mplot3d import axes3d
from scipy.signal import savgol_filter

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


ifile  = open('sample.csv', "rb")
reader = csv.reader(ifile)
results = []
rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            #print '%-8s: %s' % (header[colnum], col)
            colnum += 1
            if (colnum==1) and (len(row)>1):
                results.append(float(row[1]))
    rownum += 1
ifile.close()

my_sum=0; 
for this_num in results:
    my_sum=my_sum+float(this_num)
print "my_sum is:  ", my_sum
    
total_len=0;
for i in range(0,len(results)-1):
    total_len = total_len + sqrt(pow(float(results[i+1])-float(results[i]),2))
print "total_len is:  ", total_len


n=len(results)
D=40.0
p=np.linspace(0,100,n)

print len(results)
print len(p)

s_smooth = savgol_filter(results, 401, 2) # window size 51, polynomial order 3import matplotlib.pyplot as plt
s_smooth2 = savgol_filter(results,51,4)
s_smooth3 = smooth(results,12)

fig=plt.figure()
fig.suptitle("CSV Datapoints Smoothing and Processed")
fig.subplots_adjust(left=0.1, wspace=0.4, hspace = 0.4)
 
sub1=fig.add_subplot(221)
sub1.plot(p,results)
sub1.set_title("CSV data")
 
sub2=fig.add_subplot(222)
sub2.plot(p,s_smooth)
sub2.set_title("s_smooth")
 
sub3=fig.add_subplot(223)
sub3.plot(p,s_smooth2)
sub3.set_title("s_smooth2")
 
sub4=fig.add_subplot(224)
sub4.plot(p,s_smooth3)
sub4.set_title("s_smooth3")
 
total_len=0; total_len2=0; total_len3=0; total_len4=0; total_lenp=0;  
for i in range(0,n-1):
    total_len = total_len + sqrt(pow(results[i+1]-results[i],2) + pow(p[i+1]-p[i],2))
    total_len2 = total_len2 + sqrt(pow(s_smooth[i+1]-s_smooth[i],2) + pow(p[i+1]-p[i],2))
    total_len3 = total_len3 + sqrt(pow(s_smooth2[i+1]-s_smooth2[i],2) + pow(p[i+1]-p[i],2))
    total_len4 = total_len4 + sqrt(pow(s_smooth3[i+1]-s_smooth3[i],2) + pow(p[i+1]-p[i],2))
    total_lenp = total_lenp + (p[i+1]-p[i])
      
print "length of 'results' = ", total_len
print "length of 's_smooth' = ", total_len2
print "length of 's_smooth2' = ", total_len3
print "length of 's_smooth3' = ", total_len4
print "length of 'p' = ", total_lenp
 
plt.show()

