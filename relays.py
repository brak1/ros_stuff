#!/usr/bin/env python

import serial
import datetime

ser = serial.Serial('/dev/ttyUSB1')  # open serial port
print(ser.name)         # check which port was really used
ser.write("\xff\x00\x01")
#ser.write("\xFF\x01\x01")
#ser.write("\xFF\x02\x01")
#ser.write("\xFF\x03\x01")
#ser.write("\xFF\x04\x01")
#ser.write("\xFF\x05\x01")
#ser.write("\xFF\x06\x01")
#ser.write("\xFF\x07\x01")
#ser.write("\xFF\x08\x01")
ser.close()
print (datetime.datetime.now())


#>>> ser = serial.Serial()
#>>> ser.baudrate = 19200
#>> ser.port = 'COM1'
#>>> ser
#Serial<id=0xa81c10, open=False>(port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
#>>> ser.open()
#>>> ser.is_open
#True
#>>> ser.close()
#>>> ser.is_open
#False
