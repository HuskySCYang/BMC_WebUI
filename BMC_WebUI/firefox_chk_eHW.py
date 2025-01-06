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
	print ("")





search_elem_user = driver.find_element_by_id('userid')
search_elem_user.send_keys(user)
time.sleep(1)
search_elem_password = driver.find_element_by_id('password')
search_elem_password.send_keys(password)
time.sleep(1)
search_elem_btn = driver.find_element_by_id('btn-login')
search_elem_btn.click()
time.sleep(5)
print ("")
#__________________________________________________________________

link = driver.find_element_by_css_selector("a.small-box-footer:nth-child(4)")
link.click()






time.sleep(2)


#__________________________________________________________________
print ("RMC HW information")
print ("")
rmc_info = driver.find_element_by_css_selector("#tbl_device_info").text
print (rmc_info)
print ("")
print ("")
#__________________________________________________________________
print ("switch HW information")
print ("")
switch_info = driver.find_element_by_css_selector(".box-warning > div:nth-child(2)").text
print (switch_info)
print ("")
print ("")
#__________________________________________________________________
print ("network HW information")
print ("")
network_info = driver.find_element_by_css_selector(".box-success > div:nth-child(2)").text
print (network_info)
print ("")
print ("")	
	


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
	driver.get(url+"/#logout")  
	time.sleep(1)
	alert = driver.switch_to.alert
	alert.accept()
	time.sleep(1)
	print ("")
'''
html = requests.get('https://192.168.100.160')#,verify=False)
print (html.text)
'''
driver.close()









