#/usr/bin/python3
import os
import sys


if __name__ == "__main__":
	A = [2,3,3,4,16,16,19,28,31]
	S = sys.argv[1]
	print("parameter-1: ",S)
	if int(S) in A:
		i=0
		j=[]
		while i < len(A):
			#print (A[i])
			if int(S) == A[i]:
				j = j + [i]
			i = i + 1
		print (j)
	else:
		print ([-1],[-1])	




	A.reverse()
	print (A)
