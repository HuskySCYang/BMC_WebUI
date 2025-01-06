gui=open('config_name.log')
for line in gui.readlines():
	if "bak" in line:
		upload_file=line.strip()
	

print(upload_file)
'''
gui=open('config.log')
for line in gui.readlines():
	#upload_file=line
	if "1" in line:
		print("1")
	else:
		print("0")

'''
