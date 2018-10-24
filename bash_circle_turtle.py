#!/usr/bin/env python

# To run this: 
#  start a roscore 
#  rosrun turtlesim turtlesim_node 

import os 

bashCommand = """rostopic pub -r 100 /turtle1/cmd_vel geometry_msgs/Twist "linear:\n x: 0.5\n y: 0.0\n z: 0.0\nangular:\n x: 0.0\n y: 0.0\n z: 1.0" """ 
print bashCommand
os.system(bashCommand)
