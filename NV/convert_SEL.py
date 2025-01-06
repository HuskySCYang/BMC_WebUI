#!/usr/bin/python3

import time
import sys
import os
import configparser
#import subprocess



SEL_cmd = "ipmitool sel list"

cmd_output = os.popen(SEL_cmd)
time.sleep(1)	
target_key = "Boot"
print("Wait..")
while target_key not in cmd_output.read():
	#print("FF")
	print('FF',end='')		
	time.sleep(1)
	#cmd_output = os.popen(SEL_cmd)
	os.popen(SEL_cmd)
	#print(cmd_output.read())
	
else:
	time.sleep(1)
	print("GG")

