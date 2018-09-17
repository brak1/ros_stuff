#!/usr/bin/env python

import serial, datetime, click, time, sys, select, termios, tty

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    filename="myFile.txt"
    datafile=open(filename, 'a')

    ser1opened = False
    ser1 = serial.Serial('/dev/ttyUSB0')
    ser1.baudrate = 9600
    print(ser1.name)
    ser2opened = False
    ser2 = serial.Serial('/dev/ttyUSB1')
    ser2.baudrate = 9600
    print(ser2.name)
    
    try:
        if ser1.is_open == False:
            ser1.open();
            ser1opened = True
        if ser2.is_open == False:
            ser2.open();
            ser2opened = True
        while True:
            key = getKey()
            if key == "4":
                print key + " pressed"
                ser1.write("\xff\x01\x01")
                ser1.write("\xff\x02\x00")
                ser2.write("M0")
            elif key == "6":
                print key + " pressed"
                ser1.write("\xff\x01\x00")
                ser1.write("\xff\x02\x01")
                ser2.write("M0")
            elif key == "\x03":
                break
            else:
                print key + " pressed"
                ser1.write("\xff\x00\x00")
                data = ser2.readline()
                datafile.write(data)
            print (datetime.datetime.now())
            #time.sleep(0.5)
            #value = click.prompt('Please enter something')
            #print value
            
    except KeyboardInterrupt:
        print(" keyboard interrupt received...")
    finally:
        if ser1opened:
            ser1.close()
            print "Closed ser1"
        if ser2opened:
            ser2.close()
            print "Closed ser2"
        datafile.close()
        print "Cleaned up program and exiting"
    
    




# OTHER STUFF 
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
#ser.write("\xFF\x01\x01")
#ser.write("\xFF\x02\x01")
#ser.write("\xFF\x03\x01")
#ser.write("\xFF\x04\x01")
#ser.write("\xFF\x05\x01")
#ser.write("\xFF\x06\x01")
#ser.write("\xFF\x07\x01")
#ser.write("\xFF\x08\x01")