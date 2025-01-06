import pandas as pd
import sys


read_file = pd.read_excel(sys.argv[1],sheet_name="B001",usecols="F,I", nrows=100)
#pd.set_option("display.max_rows",500)
#print (read_file.to_string())
print (read_file)


