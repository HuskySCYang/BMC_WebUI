import sys
import os

output_lan = os.popen("ifconfig")
print(output_lan.read())
