#!/usr/bin/env python

import csv
from _ast import Num
from math import sqrt


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
            print '%-8s: %s' % (header[colnum], col)
            colnum += 1
            if (colnum==1) and (len(row)>1):
                results.append(row[1])
        if len(row)>1:
            print "row1 is: ", row[1]
    rownum += 1

ifile.close()

print "Try to math: ", results[3]+results[7]
print "Try to math: ", float(float(results[3])+float(results[7]))

my_sum=0; 
for this_num in results:
    my_sum=my_sum+float(this_num)
    
print "my_sum is:  ", my_sum
    
print results

total_len=0;
for i in range(0,len(results)-1):
    #total_len = total_len + float(results[i+1])-float(results[i]); 
    #total_len = total_len + sqrt(pow(results[i+1]-results[i],2) + pow(p[i+1]-p[i],2))
    total_len = total_len + sqrt(pow(float(results[i+1])-float(results[i]),2))
print "total_len is:  ", total_len



# sum = np.zeros(len(data[0]))
# 
# for vector in data[1:]:
#     vector = map(float, vector)
#     sum = np.add(vector, sum)

# results = []
# with open("sample.csv") as csvfile:
#     reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
#     for row in reader: # each row is a list
#         results.append(row)
#         
# print results
