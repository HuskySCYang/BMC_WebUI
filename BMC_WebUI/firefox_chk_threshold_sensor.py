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
test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_id('userid'), message='wait fail')

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

try:
	link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)')
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	link = driver.find_element_by_css_selector('.sidebar-menu > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)')
	link.click()


#link = driver.find_element_by_link_text('#fru')
#span = driver.find_element_by_css_selector("FRU Information")

#'''
#element = driver.find_element(:css, '#food span.dairy')

#search_elem_string = driver.find_element_by_class_name('box-body')
#print (search_elem_string )

#driver.get('https://192.168.100.107/#fru')  
time.sleep(5)

try:
	url = 'https://'+ip+'/#sensors/0/192'
	driver.get(url) 
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Fan_SYS0_0")
	print (sensor_info)
	print (" ")

except:
	url = 'https://'+ip+'/#sensors/0/192'
	driver.get(url)  
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Fan_SYS0_0")
	print (sensor_info)
	print (" ")


try: 
	url = 'https://'+ip+'/#sensors/0/194'
	driver.get(url)  
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Fan_SYS0_1")
	print (sensor_info)
	print (" ")

except:
	url = 'https://'+ip+'/#sensors/0/194'
	driver.get(url)  
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Fan_SYS0_1")
	print (sensor_info)
	print (" ")


try:
	url = 'https://'+ip+'/#sensors/0/196'
	driver.get(url)    
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Fan_SYS1_0")
	print (sensor_info)
	print (" ")


except:
	url = 'https://'+ip+'/#sensors/0/196'
	driver.get(url)    
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Fan_SYS1_0")
	print (sensor_info)
	print (" ")

try: 
	url = 'https://'+ip+'/#sensors/0/198'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Fan_SYS1_1")
	print (sensor_info)
	print (" ")

except: 
	url = 'https://'+ip+'/#sensors/0/198'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Fan_SYS1_1")
	print (sensor_info)
	print (" ")

try:	
	url = 'https://'+ip+'/#sensors/0/241'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("HSC_Voltage")
	print (sensor_info)
	print (" ")

except:	
	url = 'https://'+ip+'/#sensors/0/241'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("HSC_Voltage")
	print (sensor_info)
	print (" ")

try:	
	url = 'https://'+ip+'/#sensors/0/242'
	driver.get(url)    
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("HSC_Current")
	print (sensor_info)
	print (" ")

except:	
	url = 'https://'+ip+'/#sensors/0/242'
	driver.get(url)    
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("HSC_Current")
	print (sensor_info)
	print (" ")

try:
	url = 'https://'+ip+'/#sensors/0/243'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("HSC_Power")
	print (sensor_info)
	print (" ")
except:
	url = 'https://'+ip+'/#sensors/0/243'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("HSC_Power")
	print (sensor_info)
	print (" ")

try:
	url = 'https://'+ip+'/#sensors/0/170'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_CPU0")
	print (sensor_info)
	print (" ")

except:
	url = 'https://'+ip+'/#sensors/0/170'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_CPU0")
	print (sensor_info)
	print (" ")


try:
	url = 'https://'+ip+'/#sensors/0/108'
	driver.get(url)
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_CPU0_ABCD")
	print (sensor_info)
	print (" ")
except:
	url = 'https://'+ip+'/#sensors/0/108'
	driver.get(url)
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_CPU0_ABCD")
	print (sensor_info)
	print (" ")


try:
	url = 'https://'+ip+'/#sensors/0/109'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_CPU0_EFGH")
	print (sensor_info)
	print (" ")

except:
	url = 'https://'+ip+'/#sensors/0/109'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_CPU0_EFGH")
	print (sensor_info)
	print (" ")


try:
	url = 'https://'+ip+'/#sensors/0/170'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_CPU0")
	print (sensor_info)
	print (" ")

except:
	url = 'https://'+ip+'/#sensors/0/170'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_CPU0")
	print (sensor_info)
	print (" ")
	
try:	
	
	url = 'https://'+ip+'/#sensors/0/190'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_PCH")
	print (sensor_info)
	print (" ")

except:	
	
	url = 'https://'+ip+'/#sensors/0/190'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_PCH")
	print (sensor_info)
	print (" ")


	
try:	
	
	url = 'https://'+ip+'/#sensors/0/98'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_MB_Front")
	print (sensor_info)
	print (" ")
		
except:	
	
	url = 'https://'+ip+'/#sensors/0/98'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_MB_Front")
	print (sensor_info)
	print (" ")
	
try:	
	
	url = 'https://'+ip+'/#sensors/0/99'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 

	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_MB_Rear")
	print (sensor_info)
	print (" ")

except:	
	
	url = 'https://'+ip+'/#sensors/0/99'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_MB_Rear")
	print (sensor_info)
	print (" ")
	
try:	
	
	url = 'https://'+ip+'/#sensors/0/88'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_VR_CPU0_IN")
	print (sensor_info)
	print (" ")

except:	
	
	url = 'https://'+ip+'/#sensors/0/88'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_VR_CPU0_IN")
	print (sensor_info)
	print (" ")
	
try:	
	
	url = 'https://'+ip+'/#sensors/0/89'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_VR_CPU0_IO")
	print (sensor_info)
	print (" ")


except:	
	
	url = 'https://'+ip+'/#sensors/0/89'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_VR_CPU0_IO")
	print (sensor_info)
	print (" ")
try:	
	
	url = 'https://'+ip+'/#sensors/0/48'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_0")
	print (sensor_info)
	print (" ")
except:	
	
	url = 'https://'+ip+'/#sensors/0/48'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_0")
	print (sensor_info)
	print (" ")
		
try:	
	
	url = 'https://'+ip+'/#sensors/0/49'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_1")
	print (sensor_info)
	print (" ")
		
except:	
	
	url = 'https://'+ip+'/#sensors/0/49'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_1")
	print (sensor_info)
	print (" ")
		
try:	
	
	url = 'https://'+ip+'/#sensors/0/50'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_2")
	print (sensor_info)
	print (" ")
		
except:	
	
	url = 'https://'+ip+'/#sensors/0/50'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_2")
	print (sensor_info)
	print (" ")
		
try:	
	
	url = 'https://'+ip+'/#sensors/0/51'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_3")
	print (sensor_info)
	print (" ")
		
except:	
	
	url = 'https://'+ip+'/#sensors/0/51'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_3")
	print (sensor_info)
	print (" ")
		
try:	
	
	url = 'https://'+ip+'/#sensors/0/54'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_4")
	print (sensor_info)
	print (" ")
except:	
	
	url = 'https://'+ip+'/#sensors/0/54'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_4")
	print (sensor_info)
	print (" ")
		
try:	
	
	url = 'https://'+ip+'/#sensors/0/55'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_5")
	print (sensor_info)
	print (" ")
		
except:	
	
	url = 'https://'+ip+'/#sensors/0/55'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_NVMe_5")
	print (sensor_info)
	print (" ")

try:	
	url = 'https://'+ip+'/#sensors/0/52'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_M2_NVMe_0")
	print (sensor_info)
	print (" ")

except:	
	
	url = 'https://'+ip+'/#sensors/0/52'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_M2_NVMe_0")
	print (sensor_info)
	print (" ")
	
	
try:	
	
	url = 'https://'+ip+'/#sensors/0/53'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_M2_NVMe_1")
	print (sensor_info)
	print (" ")

except:	
	
	url = 'https://'+ip+'/#sensors/0/53'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_M2_NVMe_1")
	print (sensor_info)
	print (" ")
	
try:	
	
	url = 'https://'+ip+'/#sensors/0/75'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_GPU0")
	print (sensor_info)
	print (" ")
	
except:	
	
	url = 'https://'+ip+'/#sensors/0/75'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_GPU0")
	print (sensor_info)
	print (" ")
	
try:	
	
	url = 'https://'+ip+'/#sensors/0/76'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_GPU1")
	print (sensor_info)
	print (" ")
	
	
except:	
	
	url = 'https://'+ip+'/#sensors/0/76'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_GPU1")
	print (sensor_info)
	print (" ")
	
		
try:	
	
	url = 'https://'+ip+'/#sensors/0/77'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_GPU2")
	print (sensor_info)
	print (" ")
	
		
except:	
	
	url = 'https://'+ip+'/#sensors/0/77'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Temp_GPU2")
	print (sensor_info)
	print (" ")
	
		
try:	
	url = 'https://'+ip+'/#sensors/0/216'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_PVCCIN_CPU0")
	print (sensor_info)
	print (" ")
	
		
except:	
	url = 'https://'+ip+'/#sensors/0/216'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_PVCCIN_CPU0")
	print (sensor_info)
	print (" ")
	
	
try:	

	
	url = 'https://'+ip+'/#sensors/0/213'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_PVNN_PCH")
	print (sensor_info)
	print (" ")
	
except:	

	
	url = 'https://'+ip+'/#sensors/0/213'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_PVNN_PCH")
	print (sensor_info)
	print (" ")	
	
try:	
	
	
	url = 'https://'+ip+'/#sensors/0/218'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_CPU0_VCCDHV")
	print (sensor_info)
	print (" ")
	
except:	
	
	
	url = 'https://'+ip+'/#sensors/0/218'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_CPU0_VCCDHV")
	print (sensor_info)
	print (" ")	
try:	
	
	
	
	url = 'https://'+ip+'/#sensors/0/219'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P12V_AEP")
	print (sensor_info)
	print (" ")
except:	
	
	
	
	url = 'https://'+ip+'/#sensors/0/219'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail')
	print ("except retry")
	time.sleep(5) 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P12V_AEP")
	print (sensor_info)
	print (" ")
		
	
try:	
	
	
	url = 'https://'+ip+'/#sensors/0/211'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P1V05_PCH")
	print (sensor_info)
	print (" ")
except:	
	
	
	url = 'https://'+ip+'/#sensors/0/211'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail')
	print ("except retry")
	time.sleep(5) 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P1V05_PCH")
	print (sensor_info)
	print (" ")
		
try:	
	
	
	
	url = 'https://'+ip+'/#sensors/0/214'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P1V8_PCH")
	print (sensor_info)
	print (" ")
	
		
except:	
	
	
	
	url = 'https://'+ip+'/#sensors/0/214'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail')
	print ("except retry")
	time.sleep(5) 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P1V8_PCH")
	print (sensor_info)
	print (" ")
		
try:	
	
	
	url = 'https://'+ip+'/#sensors/0/217'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_PVCCIO_CPU0")
	print (sensor_info)
	print (" ")
		
except:	
	
	
	url = 'https://'+ip+'/#sensors/0/217'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail')
	print ("except retry")
	time.sleep(5) 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_PVCCIO_CPU0")
	print (sensor_info)
	print (" ")
		
try:	
	
	url = 'https://'+ip+'/#sensors/0/208'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P12V")
	print (sensor_info)
	print (" ")
	
		
except:	
	
	url = 'https://'+ip+'/#sensors/0/208'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail')
	print ("except retry")
	time.sleep(5) 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P12V")
	print (sensor_info)
	print (" ")
	
		
try:	

	
	url = 'https://'+ip+'/#sensors/0/210'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P5V")
	print (sensor_info)
	print (" ")
	
		
except:	

	
	url = 'https://'+ip+'/#sensors/0/210'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail')
	print ("except retry")
	time.sleep(5) 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P5V")
	print (sensor_info)
	print (" ")
	
		
try:	
	
	
	url = 'https://'+ip+'/#sensors/0/209'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P3V3")
	print (sensor_info)
	print (" ")
		
except:	
	
	
	url = 'https://'+ip+'/#sensors/0/209'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail')
	print ("except retry")
	time.sleep(5) 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P3V3")
	print (sensor_info)
	print (" ")
		
try:	
	
	
	
	url = 'https://'+ip+'/#sensors/0/222'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P5V_STBY")
	print (sensor_info)
	print (" ")
		
except:	
	
	
	
	url = 'https://'+ip+'/#sensors/0/222'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P5V_STBY")
	print (sensor_info)
	print (" ")
		
try:	
	
	
	
	url = 'https://'+ip+'/#sensors/0/223'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P3V3_AUX")
	print (sensor_info)
	print (" ")
	
		
except:	
	
	
	
	url = 'https://'+ip+'/#sensors/0/223'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P3V3_AUX")
	print (sensor_info)
	print (" ")
	
		
try:	
	
	
	url = 'https://'+ip+'/#sensors/0/212'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P12V_AUX")
	print (sensor_info)
	print (" ")
	
	
		
except:	
	
	
	url = 'https://'+ip+'/#sensors/0/212'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P12V_AUX")
	print (sensor_info)
	print (" ")
	
		
try:	

	
	url = 'https://'+ip+'/#sensors/0/220'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_CPU0_VNN_M")
	print (sensor_info)
	print (" ")
		
except:	

	
	url = 'https://'+ip+'/#sensors/0/220'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail')
	print ("except retry")
	time.sleep(5) 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_CPU0_VNN_M")
	print (sensor_info)
	print (" ")
	
		
	
try:	
	
	url = 'https://'+ip+'/#sensors/0/221'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_CPU0_VCCFA")
	print (sensor_info)
	print (" ")
	
except:	
	
	url = 'https://'+ip+'/#sensors/0/221'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_CPU0_VCCFA")
	print (sensor_info)
	print (" ")
	
		
	
try:	
	
	
	url = 'https://'+ip+'/#sensors/0/240'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail')
	 
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_CPU0_FIVRA")
	print (sensor_info)
	print (" ")
	
except:	
	
	
	url = 'https://'+ip+'/#sensors/0/240'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_CPU0_FIVRA")
	print (sensor_info)
	print (" ")
		
try:	
	
	
	
	url = 'https://'+ip+'/#sensors/0/215'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail')  
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P3V_BAT")
	print (sensor_info)
	print (" ")
		
except:	
	
	
	
	url = 'https://'+ip+'/#sensors/0/215'
	driver.get(url)   
	test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
	print ("except retry")
	time.sleep(5)
	sensor_info = driver.find_element_by_css_selector('.col-md-4').text
	print ("Volt_P3V_BAT")
	print (sensor_info)
	print (" ")
	
		
	



	
time.sleep(2)

#url = 'https://'+ip+'/#dashboard'
#driver.get(url)   
#test = WebDriverWait(driver,15,1).until(lambda test : driver.find_element_by_class_name('breadcrumb'), message='wait fail') 
'''	
with open("checkfru.log", "w") as fru:
	fru.write(tbl_chassis_info_string)
	fru.write(tbl_board_info_string)
	fru.write(tbl_product_info_string)
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









