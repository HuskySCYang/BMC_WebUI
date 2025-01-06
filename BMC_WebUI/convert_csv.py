
import sys
import pandas as pd
import xlrd 

#excelFile = pd.read_excel(sys.argv[1],sheet_name="B001",usecols="F,I",nrows=100)
excelFile = pd.read_excel(sys.argv[1],sheet_name="BMC_Sensors",usecols="B,D,E,F,N")
target_file = sys.argv[1].split(".xlsx")[0]
final_file = target_file + ".csv"

csv_shell = open("target_excel.log","w")
csv_shell.write(final_file)
csv_shell.close()

excelFile.to_csv(final_file)
