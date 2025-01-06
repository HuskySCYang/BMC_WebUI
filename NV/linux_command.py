#!/usr/bin/python3


import time
import sys
import os
import configparser
import subprocess


def linux_parameter():
	cmd = sys.argv[1:]
	print(cmd)
	i=0
	string=""
	while i < len(cmd):
		print (cmd[i])
		string = string + " " + cmd[i]
		i = i+1
	print(string)
	cmd_output = os.system(string)
	print(cmd_output)



def linux_command(cmd):
	#cmd_output = subprocess.run(cmd, shell=True)
	cmd_output = subprocess.check_output(cmd, shell=True)
	print(cmd_output)
	
def linux_popen(cmd):
	#cmd = ifconfig
	cmd_output = os.popen(cmd)
	print(cmd_output.read())


def Check_SEL_boot_event(SEL_cmd):
	
	while True:
		cmd_output = os.popen(SEL_cmd)
		time.sleep(1)	
		target_key = "Diagnostic"
		target_key in cmd_output
		if True:	
			print("breakaaa")		
			break

def run_cmd(cmd):
    results = []

    cmd_output = subprocess.check_output(cmd, shell=True)

    for line in cmd_output:
        results.append(line)

    
    return results

config = configparser.ConfigParser()
config.read("configuration")
bmc_ip = config.get("BMC","ip")
bmc_user = config.get("BMC","user")
bmc_password = config.get("BMC","password")
SEL_list = "ipmitool -I lanplus -H " + bmc_ip + " -U " + bmc_user + " -P " + bmc_password + " sel list  "
SEL_clear = "ipmitool -I lanplus -H " + bmc_ip + " -U " + bmc_user + " -P " + bmc_password + " sel clear "
#print(raw_6)


#linux_popen(raw_6)

#SEL_cmd = "ipmitool sel list"

linux_popen(SEL_list)
linux_parameter()
