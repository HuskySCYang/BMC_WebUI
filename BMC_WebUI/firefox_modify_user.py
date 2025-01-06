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



time.sleep(2)

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


print ("step_1: enter user management ")

link = driver.find_element_by_class_name('ion-person-stalker')
link.click()

time.sleep(5)


print ("step_2: modify user #8 ")

link = driver.find_element_by_css_selector('.col-md-12 > div:nth-child(9) > div:nth-child(1) > a:nth-child(2) > div:nth-child(2) > label:nth-child(2)')
link.click()

time.sleep(8)


print ("step_3: set user #8 name ")
add_user8 = driver.find_element_by_id('idname')
add_user8.clear()
add_user8.send_keys('Asus')
time.sleep(2)

'''
print ("step_4: set user #8 password ")
add_user8 = driver.find_element_by_id('idpassword')
add_user8.send_keys('Husky123')
time.sleep(2)



print ("step_5: confirm user #8 password ")
add_user8 = driver.find_element_by_id('idconfirm_password')
add_user8.send_keys('Husky123')
time.sleep(2)

'''

print ("step_4: enter admin login password ")
add_user8 = driver.find_element_by_id('loggedin_password')
add_user8.send_keys(password)
time.sleep(2)


'''
print ("step_4: enable user #8 ")
add_user8 = driver.find_element_by_css_selector('div.form-group:nth-child(12) > label:nth-child(1)')
add_user8.click()
time.sleep(2)

#div.form-group:nth-child(12) > label:nth-child(1) > div:nth-child(1) > ins:nth-child(2)
#div.form-group:nth-child(12) > label:nth-child(1)

print ("step_7: enable user #8 channel 1")
add_user8 = driver.find_element_by_css_selector('#idaccess > div:nth-child(2) > div:nth-child(1) > ins:nth-child(2)')
add_user8.click()
time.sleep(2)
#string: #idaccess > div:nth-child(2)
#click space: #idaccess > div:nth-child(2) > div:nth-child(1) > ins:nth-child(2)

print ("step_8: set user #8 privilege administrator")
add_user8 = driver.find_element_by_css_selector('#id_privilege_1')
select = Select(add_user8)
select.select_by_value("administrator")
time.sleep(2)

#id_privilege_1
#id_privilege_1
'''

print ("step_5: save setting")
add_user8 = driver.find_element_by_css_selector('#save')
add_user8.click()
time.sleep(4)

'''
alert = driver.switch_to.alert
alert.accept()
time.sleep(4)
'''





#__________________________________________________________________________________
try: 
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	out_link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(18) > a:nth-child(1) > span:nth-child(2)')
	out_link.click()
	time.sleep(3)
	alert = driver.switch_to.alert
	alert.accept()
	
	time.sleep(3)

except:
	driver.get(url+"/#logout")  
	time.sleep(3)
	alert = driver.switch_to.alert
	alert.accept()
	time.sleep(3)
	print ("")
'''
html = requests.get('https://192.168.100.160')#,verify=False)
print (html.text)
'''
driver.close()









