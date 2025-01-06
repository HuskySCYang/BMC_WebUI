#!/usr/bin/python3

import time
import datetime
import sys
import os
import configparser
#import subprocess



#print(datetime.datetime.now())
start_time = time.time()
print(time.asctime())

for _ in range(10):
	print(".",end="",flush=True)
	
	time.sleep(1)
print(" ",end="\n")

end_time = time.time()
print(time.asctime())

final_time = end_time - start_time
print(" ")
print("escape time: %i seconds" %(final_time))
