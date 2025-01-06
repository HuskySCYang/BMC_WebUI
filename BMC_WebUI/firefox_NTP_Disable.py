import requests
import time
from selenium import webdriver
import urllib.request 
#from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys 
import sys
import subprocess

try:
	ip = sys.argv[1]
	user = sys.argv[2]
	password = sys.argv[3]
except:
	if [ ip == " "] or [ user == " " ] or [ password == " " ] :
		print (" ")		
		print ("please check the parameter,  command: python3 firefox_chk_sensor_v02.py $bmc_ip $user $password")
		print (" ")		
		exit()




url = 'https://'+ip
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
options.add_argument("--disable-gpu")
driver = webdriver.Firefox(options=options)
#driver.maximize_window()
#driver.set_window_size(1027,768)

driver.get(url)  
time.sleep(10)

#__________________________________________________________________________________

#driver.find_element_by_name("details-button").click() 
#//*[@id="details-button"]

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




#driver.execute_script('document.body.style.MozTransform = "scale(0.7)";')
#driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
#driver.execute_script('document.body.style.zoom = "50%"')
#driver.execute_script("$('#values').css('zoom', 5);")
#driver.maximize_window()
#river.get('https://192.168.100.160/#fru') 
time.sleep(1)
#'''
print (" ")
print ("Step_0: search setting")
print (" ")
try:
	link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(6) > a:nth-child(1) > span:nth-child(2)')
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	
	link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(6) > a:nth-child(1) > span:nth-child(2)')
	link.click()



time.sleep(2)



print (" ")
print ("Step_1: Date & Time")
print (" ")

try:
	link = driver.find_element_by_css_selector('.ion-ios-clock')
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('.ion-ios-clock')
	title.click()
	
time.sleep(2)


print ("Step_2: Show time zone alert")
print (" ")
time_zone_alert = driver.find_element_by_css_selector('.content > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)').text
print (time_zone_alert)
print (" ")



print (" ")
print ("Step_3: Disable Automatic NTP Date & Time ")
print (" ")

try:
	link = driver.find_element_by_css_selector('.checked > ins:nth-child(2)')
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('.checked > ins:nth-child(2)')
	title.click()
	
time.sleep(2)

print (" ")
print ("Step_4: Save settings")
print (" ")

try:
	link = driver.find_element_by_css_selector('#save')
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('#save')
	title.click()
	
time.sleep(2)
print (" ")
alert_info_1=driver.switch_to.alert.text
print (alert_info_1)
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()
print (" ")
time.sleep(5)
print (" ")

try:
	alert_info_2=driver.switch_to.alert.text
	print (alert_info_2)
	time.sleep(5)
	alert = driver.switch_to.alert
	alert.accept()
except:

	print (" ")
	print ("Automatic logout")
	print (" ")







driver.close()








