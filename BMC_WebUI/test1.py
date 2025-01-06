import requests
import time
from selenium import webdriver
import urllib.request 
#from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys 
import sys
import subprocess
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#https://www.jianshu.com/p/604194639775

'''
time.sleep(1)
print ("")
gui=open('configuration')
for line in gui.readlines():
	result=line.find("bmcimage_new")
	if result != -1:
		#image=line[13:37]
		image = line.split("=")[1]
		target_image = image.split()[0]
		print("image: " + target_image)
			
	else:
		link=line.find("image_path")
		if link != -1:
			#path=line[11:25]
			path = line.split("=")[1]
			target_path = path.split()[0]
			print("path: "  + target_path)
			break

##
##upload image
##
update_image=target_path+target_image
print (update_image)
'''

gui=open('configuration')
for line in gui.readlines():
	result=line.find("biosimage_old")
	if result != -1:
		#image=line[13:37]
		image = line.split("=")[1]
		target_image = image.split()[0]
		print("image: " + target_image)
			
	else:
		link=line.find("image_path")
		if link != -1:
			#path=line[11:25]
			path = line.split("=")[1]
			target_path = path.split()[0]
			print("path: "  + target_path)
			break

##
##upload image
##
update_image=target_path+target_image
print (update_image)
