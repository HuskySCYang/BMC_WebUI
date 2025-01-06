import sys
import os


sensor = "PVCCIN_IIN | 18h | 36.9 | NA | NA | NA | NA | NA \
          PVCCIN_VIN | 19h | 39 | NA | NA | NA | NA | NA"
print(sensor.count("NA"))
find_string = sensor.find("20")
print (find_string)
if find_string == -1:
	print("No find")
else:
	print("find")
	
new = sensor.replace("PVCCIN","PVCCIN_CPU0",100)
print (new)
