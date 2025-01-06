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
print ("Login Successful")

#__________________________________________________________________
#__________________________________________________________________
#Dual RMC FW information
try:
	link = driver.find_element_by_css_selector(".sidebar-menu > li:nth-child(16) > a:nth-child(1) > span:nth-child(2)")
	link.click()
	
	
except:
	title = driver.find_element_by_css_selector('#sidebar-toggle')
	title.click()
	
	link = driver.find_element_by_css_selector(".sidebar-menu > li:nth-child(16) > a:nth-child(1) > span:nth-child(2)")
	link.click()


time.sleep(1)
print ("")
print ("")


##
##go to update page
##
print ("go to update page")
update_bmc= driver.find_element_by_css_selector('div.col-md-3:nth-child(6) > a:nth-child(1) > div:nth-child(1) > i:nth-child(1)')
update_bmc.click()


time.sleep(5)
print ("")




update_info_1 = driver.find_element_by_css_selector('.box-body').text
print (update_info_1)	
	
time.sleep(1)
print ("")
gui=open('configuration')
for line in gui.readlines():
	result=line.find("bmcimage_old")
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
try:
	update_bmc = driver.find_element_by_css_selector('#mainfirmware_image')
	update_bmc.send_keys(update_image)


except:
	
	print ("Select update image fail")


gui.close




print ("")
time.sleep(10)
print ("")

try:    
	print ("Detect the btnFirmwareChecks#1")
	link = driver.find_element_by_css_selector('#btnFirmwareChecks')
	link.click()
	time.sleep(5)
	
except:
	print ("Detect the btnFirmwareChecks#2")
	link = driver.find_element_by_css_selector('#btnFirmwareChecks')
	link.click()
	time.sleep(5)




print ("")
update_info_2 = driver.find_element_by_css_selector('div.box:nth-child(3)').text
print (update_info_2)	
print ("")
print ("")

time.sleep(5)
##
##select update image 1/2
##
image_select = driver.find_element_by_css_selector('#idimage_update')
bank = Select(image_select)
#Image both
bank.select_by_value("3")

print ("")
time.sleep(5)
print ("")




'''
##
##preserved configuration
##
print ("Preserved Configuration: Yes")

try:
	preserved = driver.find_element_by_css_selector('.iCheck-helper')
	preserved.click()
	
	
except:
	print ("preserved configuration fail")
time.sleep(2)
'''





##
##start to udpate
##
link = driver.find_element_by_css_selector('#start')
link.click()
print ("")
print ("")

##
##confirm update
##
WebDriverWait(driver,60,1).until(EC.alert_is_present())
alert_info=driver.switch_to.alert.text
print (alert_info)
time.sleep(10)
alert = driver.switch_to.alert
alert.accept()
print("")
print("wait for upload image done")
print("")
#time.sleep(120)
print("")
print(time.ctime())

for i in range(int(120)):
	print(".",end='',flush=True)
	time.sleep(1)
print("")
print(time.ctime())
print("")
print("")
##
##wait for upload image done
##

try: 
	start_update = WebDriverWait(driver,120,1).until(lambda start_update : driver.find_element_by_css_selector('#firmware_update_desc > p:nth-child(3)'), message='wait Upload image fail #1')
	time.sleep(5)
	update_info_2 = driver.find_element_by_css_selector('#firmware_update_desc > p:nth-child(3)').text
	print("")
	print (update_info_2)	
	print("")
	print ("Upload image done ")
except:
	start_update = WebDriverWait(driver,30,1).until(lambda start_update : driver.find_element_by_css_selector('#firmware_update_desc > p:nth-child(3)'), message='wait Upload image fail #2')
	time.sleep(5)
	update_info_2 = driver.find_element_by_css_selector('#firmware_update_desc > p:nth-child(3)').text
	print("")
	print (update_info_2)	
	print("")
	print ("Upload image done ")


#firmware_update_desc > p:nth-child(3)


				
		
time.sleep(5)
print ("")
## check update items
print ("Check Full Flash item")
print ("")
image_updte_selector = driver.find_element_by_css_selector('div.col-xs-6:nth-child(2)').text

if "Full" in image_updte_selector:
##
##Full Flash
##	
	print ("")
	print ("Select Full Flash ")
	try:
		Full_Flash = driver.find_element_by_css_selector('div.col-xs-6:nth-child(2) > div:nth-child(1) > ins:nth-child(2)')
		Full_Flash.click()
	except:
		print ("Select Full Flash fail..")
	
time.sleep(2)




##
##upload image to BMC done 
##
print ("")
print ("")
print ("Start to update image")
print ("")
print ("")
link = driver.find_element_by_css_selector('#start')
link.click()
##
##start to update
##
WebDriverWait(driver,20,1).until(EC.alert_is_present())
alert_info=driver.switch_to.alert.text
print (alert_info)
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
	


##
##update done and wait for BMC rebooting
##

print ("")
print ("")
print ("Wait for BMC update and reboot completed")
print ("")
print ("")

WebDriverWait(driver,200,1).until(EC.alert_is_present())
alert_info=driver.switch_to.alert.text
print (alert_info)
alert = driver.switch_to.alert
alert.accept()
print ("")
print ("")



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


'''
driver.close()









