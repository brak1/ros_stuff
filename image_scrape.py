#!/usr/bin/env python

import urllib
import time
import os

while(True):
	os.system('clear')
	timestr = time.strftime("%Y%m%d-%H%M%S")
	savefilename = "./data/" + "img_" + timestr + ".jpg"
	urllib.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cheeseburger.jpg/1200px-Cheeseburger.jpg", savefilename)
	print "\n" + savefilename + " image file saved"
	time.sleep(5)



