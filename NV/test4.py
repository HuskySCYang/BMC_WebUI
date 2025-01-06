import sys
import os


a = {
	"g1": "123",
	"g2": "456",
	"g3": "789",
	"g4": "abc",
	"g5": "def",
}

print(a)

b = {
	"g6": "99999",
	"g7": "11111"
}
print(b)



a.update(b)
print (a)
del a["g6"]

print(a)

c = {"g6":"123546"}
a.update(c)
print(a)
