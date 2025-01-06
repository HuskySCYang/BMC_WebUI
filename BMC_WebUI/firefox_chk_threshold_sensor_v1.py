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



localtime = time.localtime()
result = time.strftime("%y-%m-%d %I:%M:%S %p", localtime)
print (result)

try:
	ip = sys.argv[1]
	user = sys.argv[2]
	password = sys.argv[3]
	target_file = sys.argv[4]
except:
	if [ ip == " "] or [ user == " " ] or [ password == " " ] :
		print (" ")		
		print ("please check the parameter,  command: python3 firefox_chk_sensor_v02.py $bmc_ip $user $password")
		print (" ")		
		exit()




url = 'https://'+ip
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Firefox(options=options)


driver.get(url)  
test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_id('userid'), message='wait fail')

#__________________________________________________________________________________



try:
	search_btn_1 = driver.find_element_by_id('details-button')
	search_btn_1.click()
	time.sleep(5)
	search_btn_2 = driver.find_element_by_id('proceed-link')
	search_btn_2.click()
	time.sleep(5)
except:
	print ("No SSL Certificates")





search_elem_user = driver.find_element_by_id('userid')
search_elem_user.send_keys(user)
time.sleep(1)
search_elem_password = driver.find_element_by_id('password')
search_elem_password.send_keys(password)
time.sleep(1)
search_elem_btn = driver.find_element_by_id('btn-login')
search_elem_btn.click()
time.sleep(5)

try:
	link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)')
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)')
	link.click()


time.sleep(5)


target = open(target_file)
for line in target:
	print (line)
	target_srting = line.split(",")
	final_string = list(target_srting)
	sensor_name = final_string[0]
	sensor_number = final_string[1]
	print ("sensor_name:" + sensor_name + "," + "sensor_number:" + sensor_number)
	i_keyword=0
	while True: 
		try:
			url = 'https://'+ip+'/#sensors/0/'+sensor_number
			#print (url)
			driver.get(url) 
			test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_id('change-threshold'), message='wait fail') 
			test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('box-title'), message='wait fail')
			time.sleep(5)
			#sensor_info = driver.find_element_by_css_selector('#sensor-content').text
			sensor_info = driver.find_element_by_id('sensor-content').text
			if 'Thresholds' in sensor_info:
				print (sensor_name)
				print (sensor_info)
				print (" ")
				#i_keyword = 1
				break
		except:
			time.sleep(5)
			url = 'https://'+ip+'/#sensors/0/'+sensor_number
			print (url)
			driver.get(url) 
			test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_id('change-threshold'), message='wait fail') 
			test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('box-title'), message='wait fail')
			time.sleep(5)
			#sensor_info = driver.find_element_by_css_selector('#sensor-content').text
			sensor_info = driver.find_element_by_id('sensor-content').text
			if 'Thresholds' in sensor_info:
				print (sensor_name)
				print (sensor_info)
				print (" ")
				#i_keyword = 1
				break
localtime = time.localtime()
result = time.strftime("%y-%m-%d %I:%M:%S %p", localtime)
print (result)



#__________________________________________________________________________________
try: 
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	out_link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(18) > a:nth-child(1) > span:nth-child(2)')
	out_link.click()
	time.sleep(2)
	alert = driver.switch_to.alert
	alert.accept()
	
	time.sleep(2)

except:
	url = 'https://'+ip
	driver.get(url+"/#logout")  
	time.sleep(5)
	alert = driver.switch_to.alert
	alert.accept()
	time.sleep(1)
	print ('end')
'''
html = requests.get('https://192.168.100.160')#,verify=False)
print (html.text)
'''


localtime = time.localtime()
result = time.strftime("%y-%m-%d %I:%M:%S %p", localtime)
print (result)


driver.close()



