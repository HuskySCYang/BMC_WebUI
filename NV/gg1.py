import os
import sys
import subprocess

output_1 = os.popen("ifconfig")
print(output_1.read())

output_2 = subprocess.check_output("ifconfig")
#print (str(output_2).split('\\n'))
A = str(output_2).split('\\n')
print(A[0])
print(A[2])

