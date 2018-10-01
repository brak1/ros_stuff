#!/usr/bin/env python

import csv

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
            results.append(col)
            
    rownum += 1

ifile.close()

print results



# results = []
# with open("sample.csv") as csvfile:
#     reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
#     for row in reader: # each row is a list
#         results.append(row)
#         
# print results
