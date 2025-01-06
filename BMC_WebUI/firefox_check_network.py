import requests
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support import ui
import urllib.request 
#from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys 
import sys
import subprocess
#import selenium

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
#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver.maximize_window()
#driver.set_window_size(1024,768)
#driver.execute_script('document.body.style.Moztransform = "scale(0.8)";')
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
print ("step_0: search setting")

try:
	link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(6) > a:nth-child(1) > span:nth-child(2)')
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	
	link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(6) > a:nth-child(1) > span:nth-child(2)')
	link.click()



time.sleep(5)

#driver.get('https://192.168.100.164/#settings/users/edit/8') 
'''
try:
	link = driver.find_element_by_xpath("//*[contains(text(), 'Settings')]")
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	link = driver.find_element_by_xpath("//*[contains(text(), 'Settings')]")
	link.click()
'''


print ("step_1: enter Network Setting ")

link = driver.find_element_by_css_selector('.fa-sitemap')
link.click()

time.sleep(5)
print ("step_2: Network IP Setting ")

link = driver.find_element_by_css_selector('.fa-sitemap')
link.click()

time.sleep(2)

print ("step_3: Get IPv6 status")

ipv6_info = driver.find_element_by_css_selector('.box-body').text
print (ipv6_info)

print ("step_4: Cancel IPv6 option")

link = driver.find_element_by_css_selector('div.form-group:nth-child(11) > label:nth-child(2) > div:nth-child(1) > ins:nth-child(2)')
link.click()

time.sleep(2)

print ("step_5: save setting")
link = driver.find_element_by_css_selector('#save')
link.click()
time.sleep(5)

alert = driver.switch_to.alert
alert.accept()
time.sleep(10)


alert = driver.switch_to.alert
alert.accept()
time.sleep(10)


print (url)

driver.get(url)  
#driver.refresh()


time.sleep(18)

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
print ("step_6: search setting")

try:
	link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(6) > a:nth-child(1) > span:nth-child(2)')
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	
	link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(6) > a:nth-child(1) > span:nth-child(2)')
	link.click()



time.sleep(5)

#driver.get('https://192.168.100.164/#settings/users/edit/8') 
'''
try:
	link = driver.find_element_by_xpath("//*[contains(text(), 'Settings')]")
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	link = driver.find_element_by_xpath("//*[contains(text(), 'Settings')]")
	link.click()
'''


print ("step_7: enter Network Setting ")

link = driver.find_element_by_css_selector('.fa-sitemap')
link.click()

time.sleep(5)
print ("step_8: Network IP Setting ")

link = driver.find_element_by_css_selector('.fa-sitemap')
link.click()

time.sleep(2)


print ("step_9: Get IPv6 status")

ipv6_info = driver.find_element_by_css_selector('.box-body').text
print (ipv6_info)


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

driver.close()









