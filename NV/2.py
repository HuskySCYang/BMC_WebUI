#/usr/bin/python3
import time
import sys

	
A=[2,4,6,8,10,12]
B=[1,3,5,7,9,11]
'''
C=set(A)|set(B)
C=list(C)
C.sort()
print(C)
'''
L_A = len(A)
L_B = len(B)
C = []
i=0
while i < L_A:
	print(i,A[i],B[i])
	if A[i] > B[i]:
		C = C + [B[i]] + [A[i]] 
	else:
		C = C + [A[i]] + [B[i]] 
	i=i+1
print(C)

