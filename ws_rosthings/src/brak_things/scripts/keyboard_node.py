#!/usr/bin/env python

import serial, datetime, click, time, sys, select, termios, tty
import rospy
from std_msgs.msg import String


def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    try:
    
        pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
    #     while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
      
        while True:
            key = getKey()
            if key == "4":
                print key + " pressed"
                pub.publish(key)

            elif key == "6":
                print key + " pressed"
                pub.publish(key)

            elif key == "\x03":
                break
            
            else:
                print key + " pressed"
                pub.publish(key)
    
    except KeyboardInterrupt:
        print(" keyboard interrupt received...")
    finally:
        print "Cleaned up program and exiting"
