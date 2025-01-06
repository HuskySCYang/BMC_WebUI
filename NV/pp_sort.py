#/usr/bin/python3
import time
import sys

	
A=[ 2,16,19,28,31,32,39,46,48 ]
B=[ 1,8,14,17,30,40,45 ]

L_A=len(A)
L_B=len(B)
C=[]


for i in range(L_B):
	k=0
	for j in range(L_A):
		
		if B[i] > A[j]:
			k=k+1
		print(i,B[i],j,A[j],k)
	A.insert(k,B[i])
	L_A=len(A)
	print(A)
			

'''
[1, 2, 8, 14, 16, 17, 19, 28, 30, 31, 32, 39, 40, 45, 46, 48]

'''

