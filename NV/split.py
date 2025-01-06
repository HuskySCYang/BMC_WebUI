

A = "May 90 80 72"
A = "1983 90 80 72"
name,*line =  A.split()
print(name)
print(line)
print (A.split())

sum = 0
for i in range(2):
	sum = sum + float(line[i])
	print (sum)
print (format(sum/3,".2f"))


print (line)
print (list(map(float, line)))
