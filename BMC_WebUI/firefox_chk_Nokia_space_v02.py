import requests
import time
from selenium import webdriver
import urllib.request 
#from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys 
import sys
import subprocess
import os

try:
	ip = sys.argv[1]
	user = sys.argv[2]
	password = sys.argv[3]
except:
	if [ ip == " " ] or [ user == " " ] or [ password == " " ] :
		print (" ")		
		print ("please check the parameter,  command: python3 firefox_chk_Nokia_space_v01.py $bmc_ip $user $password")
		print (" ")		
		exit()

'''
#cmd="ipmitool -I lanplus -H $ip -U $user -P $password "
ipmi_command = "ipmitool -I lanplus -H " + ip + " -U " + user + " -P " + password + " lan print"
#print (ipmi_command)
#output = subprocess.check_output(ipmi_command, shell=True)
output = subprocess.getoutput(ipmi_command)
'''
ipmi_command = "ipmitool -I lanplus -H " + ip + " -U " + user + " -P " + password + " lan print" + " > lan.log"

os.system(ipmi_command)

#target="MAC Address"
with open("lan.log", "r") as mac:
	content = mac.readlines()
	#print (content)
	for target in content:
		if "MAC Address" in target:
			#print ("MAC Address: " + target[26:43])
			Nokia_mac = target[26:43]
			with open("Nokia.log", "w") as Nokia:
				Nokia.write(Nokia_mac)





with open("Nokia.log", "r") as Nokia:
	content = Nokia.read()
	#print (content)

print (content)

'''
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
'''

url = 'https://macaddress.io/'
#url = 'https://google.com'
'''
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
'''
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
#driver = webdriver.Chrome()
options.add_argument("--disable-gpu")
driver = webdriver.Firefox(options=options)
#driver.maximize_window()
#driver.set_window_size(1027,768)

driver.get(url)  
time.sleep(10)

#__________________________________________________________________________________



search_elem_user = driver.find_element_by_name('mac-address-value')
search_elem_user.send_keys(content)
time.sleep(1)

search_elem_btn = driver.find_element_by_css_selector(".green-btn")
search_elem_btn.click()
time.sleep(5)
'''


.mac-address-report
'''


	
mac_info = driver.find_element_by_class_name('mac-address-report').text
print (mac_info)

	
time.sleep(2)
	
with open("check_mac.log", "w") as nokia:
	nokia.write(mac_info)
	
	
time.sleep(2)



driver.close()












		


