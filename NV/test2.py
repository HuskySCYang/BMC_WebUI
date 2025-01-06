import sys
import os

test_list = [ "a", "b", "c", "d" ]
print(test_list)
string_list = ":".join(test_list)
print(string_list)

sel = "15 | 10/17/2024 | 12:49:49 PM UTC | Fan Fan2_Inlet | Lower Critical going low  | Asserted | Reading 0 < Threshold 516 RPM"

target = sel.split("|")
number = len(target)
for i in range(number):
	print (target[i],end="")
print("")

'''
result:
root@srd7-sqa:~/Desktop/NV# python3 test2.py 
['a', 'b', 'c', 'd']
a:b:c:d
15  10/17/2024  12:49:49 PM UTC  Fan Fan2_Inlet  Lower Critical going low   Asserted  Reading 0 < Threshold 516 RPM
root@srd7-sqa:~/Desktop/NV# 


'''
