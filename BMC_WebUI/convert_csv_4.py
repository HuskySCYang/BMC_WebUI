import openpyxl
import csv
ob = csv.writer(open("sample.csv",'w', newline = ""))
data = openpyxl.load_workbook('ASUS.xlsx').active
for r in data.rows:
    row = [a.value for a in r]
    ob.writerow(row)
