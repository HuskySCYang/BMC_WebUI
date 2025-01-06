
import sys
import pandas as pd
import xlrd 


'''
excel=open('configuration')
for line in excel.readlines():
	result=line.find("sdr_table_sensor")
	if result != -1:
		print (line)
		page = line.split("=")[1]
		print (page)
		#target_page = page.split()[0]
		#print("Page: " + target_page)
'''		
		
#excelFile = pd.read_excel(sys.argv[1],sheet_name="B001",usecols="A,B,N,O,P,Q,R,T,U,V,W,X",nrows=100)
excelFile = pd.read_excel(sys.argv[1],sheet_name="Sensor_list",usecols="A,B,N,O,P,Q,R,T,U,V,W,X")
target_file = sys.argv[1].split(".xlsx")[0]
final_file = target_file + ".csv"
csv_shell = open("sdr_excel.log","w")
csv_shell.write(final_file)
csv_shell.close()
excelFile.to_csv(final_file)

