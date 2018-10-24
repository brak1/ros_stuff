#!/usr/bin/env python

# To run this: 
#  start a roscore 
#  rosrun turtlesim turtlesim_node 

import os 
import subprocess

bashCommand = """rostopic list > rostopics.txt""" 
print bashCommand
os.system(bashCommand)

rostopicsfile = open("rostopics.txt", "rb") 
topics = rostopicsfile.readlines()
for line in topics: 
    print line

print "Something new: " 

#read line from rostopicsfile; use to append to the desired file with >> operator

