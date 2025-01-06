#/usr/bin/python3
import time
import sys
from rembg import remove
from PIL import Image


input_path="testjpg.jpg"
output_path="good.png"
inp = Image.open(input_path)
output = remove(inp) 
output.save(output_path)


