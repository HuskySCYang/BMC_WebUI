import time
import sys
import subprocess
import os

delay = sys.argv[1]
print("")
print(time.ctime())

for i in range(int(delay)):
	print(".",end='',flush=True)
	time.sleep(1)
print("")
print(time.ctime())
print("")
