#!/usr/bin/env python

import socket, datetime, termios, sys, tty, select


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
#s.close()

print "received data:", data

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    while True:
        key = getKey()
        if key == "4":
            s.send(key)
            print key + " pressed"
        elif key == "6":
            s.send(key)
            print key + " pressed"
        elif key == "\x03":
            s.close()
            break
        else:
            print key + " pressed"
        print (datetime.datetime.now())
    
