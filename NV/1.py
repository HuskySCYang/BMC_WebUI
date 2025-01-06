#/usr/bin/python3
import time
import sys

	
A=[16,2,28,19,32,39,31,3]
B=[14,8,1,17,70,11,45]
'''
C=set(A)|set(B)
C=list(C)
C.sort()
print(C)
'''
A=A+B

L_A = len(A)
L_B = len(B)

C = []

for _ in range(0,L_A):
	C = C + [_]
print(C)

for c in A:
	i=0
	j=0	
	while i < L_A:
		
		if c > A[i]:
			j=j+1
		print (i,c,A[i],j)
		
		i=i+1
	C[j] = c
		
print (C)
	
	
	
