#!/usr/bin/python3

import time
import sys
import os
import configparser
#import subprocess


config = configparser.ConfigParser()
config.read("configuration")
bmc_ip = config.get("BMC","ip")
bmc_user = config.get("BMC","user")
bmc_password = config.get("BMC","password")
raw_6 = "ipmitool -I lanplus -H " + bmc_ip + " -U " + bmc_user + " -P " + bmc_password + " raw 0x06 0x01  "

print(bmc_ip)
print(bmc_user)
print(bmc_password)
print(raw_6)

start_time = time.time()
print(time.asctime())
'''
SEL_cmd = "ipmitool sel list 2> boot_event.log 1> boot_event.log"
print(" ")
cmd_output = os.popen(SEL_cmd)

boot_event = open("boot_event.log", "r")

time.sleep(1)	
target_key = "OS Boot #0x02"
print("Wait for boot event....")

while target_key not in boot_event.read():
	print(".",end="",flush=True)
	time.sleep(1)
	cmd_output = os.popen(SEL_cmd)
	boot_event = open("boot_event.log", "r")
	
	#if target_key in boot_event.read():
	#	break
else:
	time.sleep(1)
	print(" ")
	print("Boot event found !!")
	print(" ")	

print(" ",end="\n")

end_time = time.time()
print(time.asctime())
print(" ")
boot_event = open("boot_event.log", "r")
print(boot_event.read())
print(" ")
final_time = end_time - start_time
print(" ")
print("executed time: %i seconds" %(final_time))
print(" ")

'''
