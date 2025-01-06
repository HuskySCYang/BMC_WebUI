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
test = WebDriverWait(driver,10,1).until(lambda test : driver.find_element_by_id('userid'), message='wait fail')
#time.sleep(10)

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
#__________________________________________________________________
#
#Go to PLDM
try:						  
	link = driver.find_element_by_css_selector(".sidebar-menu > li:nth-child(10) > a:nth-child(1) > span:nth-child(2)")
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	
	link = driver.find_element_by_css_selector(".sidebar-menu > li:nth-child(10) > a:nth-child(1) > span:nth-child(2)")
	link.click()


time.sleep(3)
print ("")
print ("")



#Go to PLDM > FRU
try:						  
	link = driver.find_element_by_css_selector("div.col-md-3:nth-child(2) > a:nth-child(1) > span:nth-child(2)")
	link.click()
	
	
except:
		
	link = driver.find_element_by_css_selector("div.col-md-3:nth-child(2) > a:nth-child(1) > span:nth-child(2)")
	link.click()


time.sleep(3)
#Go to PLDM > FRU > EID_info
try:						  
	EID_info = driver.find_element_by_css_selector("div.box-body:nth-child(1)").text
	print ("")
	print (EID_info)
	print ("")
	
except:
		
	EID_info = driver.find_element_by_css_selector("div.box-body:nth-child(1)").text
	print ("")
	print (EID_info)
	print ("")



'''
EID_info_1 = driver.find_element_by_css_selector('#select2-idgroup_by_eid-container')
select = Select(EID_info_1)
select.select_by_value("administrator")
time.sleep(2)
'''











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









