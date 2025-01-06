import requests
import time
from selenium import webdriver
import urllib.request 
#from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys 
import sys
import subprocess
import time
import os


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


os.system('./ATC_RMC_020.674_1.sh ')




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
#driver = webdriver.Chrome()
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
	print (" ")





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
#.sidebar-menu > li:nth-child(3) > a:nth-child(1) > span:nth-child(2)

try:
	title = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(3) > a:nth-child(1) > span:nth-child(2)')
	title.click()
	
	
except:
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	title = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(3) > a:nth-child(1) > span:nth-child(2)')
	title.click()


#link = driver.find_element_by_link_text('#fru')
#span = driver.find_element_by_css_selector("FRU Information")

#'''
#element = driver.find_element(:css, '#food span.dairy')

#search_elem_string = driver.find_element_by_class_name('box-body')
#print (search_elem_string )

#driver.get('https://192.168.100.107/#fru')  
time.sleep(1)

title = driver.find_element_by_css_selector('#baseboard-tab')
title.click()
time.sleep(2)

title = driver.find_element_by_css_selector('#reset_switch')
title.click()
time.sleep(1)
alert = driver.switch_to.alert
alert.accept()
time.sleep(0.5)
alert = driver.switch_to.alert
alert.accept()
time.sleep(0.5)

os.system('./ATC_RMC_020.674_2.sh')



#__________________________________________________________________________________
try: 
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	out_link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(18) > a:nth-child(1) > span:nth-child(2)')
	out_link.click()
	time.sleep(1)
	alert = driver.switch_to.alert
	alert.accept()
	time.sleep(1)

except:
	driver.get(url+"/#logout")  
	time.sleep(1)
	alert = driver.switch_to.alert
	alert.accept()
	time.sleep(1)
	print ('Logout WebGUI')
'''
html = requests.get('https://192.168.100.160')#,verify=False)
print (html.text)
'''
driver.close()









